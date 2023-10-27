import os
import textwrap
from typing import Optional

import aiohttp
from aiohttp.client_exceptions import ClientResponseError
from pydantic import validate_arguments

from stabilityai.constants import (
    DEFAULT_GENERATION_ENGINE,
    DEFAULT_STABILITY_API_HOST,
    DEFAULT_STABILITY_CLIENT_ID,
    DEFAULT_STABILITY_CLIENT_VERSION,
    DEFAULT_UPSCALE_ENGINE,
)
from stabilityai.exceptions import (
    ThisFunctionRequiresAPrompt,
    YouNeedToUseAContextManager,
    figure_out_exception,
)
from stabilityai.models import (
    AccountResponseBody,
    BalanceResponseBody,
    CfgScale,
    ClipGuidancePreset,
    DiffuseImageHeight,
    DiffuseImageWidth,
    Engine,
    Extras,
    ImageToImageRequestBody,
    ImageToImageResponseBody,
    ImageToImageUpscaleRequestBody,
    ImageToImageUpscaleResponseBody,
    InitImage,
    InitImageMode,
    InitImageStrength,
    ListEnginesResponseBody,
    Sampler,
    Samples,
    Seed,
    SingleTextPrompt,
    Steps,
    StylePreset,
    TextPrompt,
    TextPrompts,
    TextToImageRequestBody,
    TextToImageResponseBody,
    UpscaleImageHeight,
    UpscaleImageWidth,
)
from stabilityai.utils import serialize_for_form


class AsyncStabilityClient:
    def __init__(
        self,
        api_host: str = os.environ.get("STABILITY_API_HOST", DEFAULT_STABILITY_API_HOST),
        api_key: Optional[str] = os.environ.get("STABILITY_API_KEY"),
        client_id: str = os.environ.get("STABILITY_CLIENT_ID", DEFAULT_STABILITY_CLIENT_ID),
        client_version: str = os.environ.get(
            "STABILITY_CLIENT_VERSION", DEFAULT_STABILITY_CLIENT_VERSION
        ),
        organization: Optional[str] = os.environ.get("STABILITY_CLIENT_ORGANIZATION"),
    ) -> None:
        self.api_host = api_host
        self.api_key = api_key
        self.client_id = client_id
        self.client_version = client_version
        self.organization = organization

    async def __aenter__(self):
        self.session = await aiohttp.ClientSession(
            base_url=self.api_host,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {self.api_key}",
                "Stability-Client-ID": self.client_id,
                "Stability-Client-Version": self.client_version,
                **({"Organization": self.organization} if self.organization else {}),
            },
            raise_for_status=True,
        ).__aenter__()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self.session.__aexit__(exc_type, exc_val, exc_tb)

    async def get_engines(self) -> ListEnginesResponseBody:
        res = await self.session.get("/v1/engines/list")
        return await res.json()

    async def get_account(self) -> AccountResponseBody:
        res = await self.session.get("/v1/user/account")
        return await res.json()

    async def get_account_balance(self) -> BalanceResponseBody:
        res = await self.session.get("/v1/user/balance")
        return await res.json()

    def _oops_no_session(self):
        if not self.session:
            raise YouNeedToUseAContextManager(
                textwrap.dedent(
                    f"""\
                {self.__class__.__name__} keeps a aiohttp.ClientSession under
                the hood and needs to be closed when you're done with it. But
                since there isn't an async version of __del__ we have to use
                __aenter__/__aexit__ instead. Apologies.

                Instead of

                    myclient = {self.__class__.__name__}()
                    myclient.text_to_image(...)
                                
                Do this

                    async with {self.__class__.__name__} as myclient:
                        myclient.text_to_image(...)

                Note that it's `async with` and not `with`.
                """
                )
            )

    def _normalize_text_prompts(
        self, text_prompts: Optional[TextPrompts], text_prompt: Optional[SingleTextPrompt]
    ):
        if not bool(text_prompt) ^ bool(text_prompts):
            raise ThisFunctionRequiresAPrompt(
                textwrap.dedent(
                    f"""\
                    You must provide one of text_prompt and text_prompts.

                    Do this

                        stability.text_to_image(
                            text_prompt="A beautiful sunrise"
                        )

                    Or this

                        from stabilityai.models import TextPrompt

                        stability.text_to_image(
                            text_prompts=[
                                TextPrompt(text="A beautiful sunrise", weight=1.0)
                            ],
                        )
                    """
                )
            )

        text_prompts = text_prompts or [TextPrompt(text=text_prompt)]
        return text_prompts

    @validate_arguments
    async def text_to_image(
        self,
        text_prompts: Optional[TextPrompts] = None,
        text_prompt: Optional[SingleTextPrompt] = None,
        *,
        engine: Optional[Engine] = None,
        cfg_scale: Optional[CfgScale] = None,
        clip_guidance_preset: Optional[ClipGuidancePreset] = None,
        height: Optional[DiffuseImageHeight] = None,
        sampler: Optional[Sampler] = None,
        samples: Optional[Samples] = None,
        seed: Optional[Seed] = None,
        steps: Optional[Steps] = None,
        style_preset: Optional[StylePreset] = None,
        width: Optional[DiffuseImageWidth] = None,
        extras: Optional[Extras] = None,
    ):
        self._oops_no_session()

        text_prompts = self._normalize_text_prompts(text_prompts, text_prompt)
        engine_id = engine.id if engine else DEFAULT_GENERATION_ENGINE

        request_body = TextToImageRequestBody(
            cfg_scale=cfg_scale,
            clip_guidance_preset=clip_guidance_preset,
            height=height,
            sampler=sampler,
            samples=samples,
            seed=seed,
            steps=steps,
            style_preset=style_preset,
            text_prompts=text_prompts,
            width=width,
            extras=extras,
        )

        try:
            res = await self.session.post(
                f"/v1/generation/{engine_id}/text-to-image",
                headers={"Content-Type": "application/json"},
                data=request_body.json(
                    exclude_defaults=True, exclude_none=True, exclude_unset=True
                ),
            )
        except ClientResponseError as e:
            raise figure_out_exception(e) from e

        return TextToImageResponseBody.parse_obj(await res.json())

    async def text_to_image_simple(
        self,
        prompt: str,
        style_preset: Optional[StylePreset] = StylePreset.digital_art,
        n: int = 1,
        size: str = "512x512",
    ):
        """
        An OpenAI SDK style call that makes it easy to migrate.
        """

        dim = int(size.split("x")[0])

        return await self.text_to_image(
            text_prompts=[TextPrompt(text=prompt)],
            style_preset=style_preset,
            samples=n,
            width=dim,
            height=dim,
        )

    @validate_arguments(config={"arbitrary_types_allowed": True})
    async def image_to_image(
        self,
        init_image: InitImage,
        text_prompts: Optional[TextPrompts] = None,
        text_prompt: Optional[SingleTextPrompt] = None,
        *,
        init_image_mode: Optional[InitImageMode] = None,
        image_strength: InitImageStrength,
        engine: Optional[Engine] = None,
        cfg_scale: Optional[CfgScale] = None,
        clip_guidance_preset: Optional[ClipGuidancePreset] = None,
        sampler: Optional[Sampler] = None,
        samples: Optional[Samples] = None,
        seed: Optional[Seed] = None,
        steps: Optional[Steps] = None,
        style_preset: Optional[StylePreset] = None,
        extras: Optional[Extras] = None,
    ):
        self._oops_no_session()

        text_prompts = self._normalize_text_prompts(text_prompts, text_prompt)
        engine_id = engine.id if engine else DEFAULT_GENERATION_ENGINE

        request_body = ImageToImageRequestBody(
            cfg_scale=cfg_scale,
            clip_guidance_preset=clip_guidance_preset,
            init_image=init_image,
            init_image_mode=init_image_mode,
            image_strength=image_strength,
            sampler=sampler,
            samples=samples,
            seed=seed,
            steps=steps,
            style_preset=style_preset,
            text_prompts=text_prompts,
            extras=extras,
        )

        form = aiohttp.FormData()
        form_data = serialize_for_form(request_body.dict())

        for k, v in form_data.items():
            form.add_field(k, v)

        try:
            res = await self.session.post(
                f"/v1/generation/{engine_id}/image-to-image",
                data=form,
            )
        except ClientResponseError as e:
            raise figure_out_exception(e) from e

        return ImageToImageResponseBody.parse_obj(await res.json())

    @validate_arguments(config={"arbitrary_types_allowed": True})
    async def image_to_image_upscale(
        self,
        image: InitImage,
        *,
        engine: Optional[Engine] = None,
        width: Optional[UpscaleImageWidth] = None,
        height: Optional[UpscaleImageHeight] = None,
    ):
        self._oops_no_session()

        engine_id = engine.id if engine else DEFAULT_UPSCALE_ENGINE

        request_body = ImageToImageUpscaleRequestBody(image=image, width=width, height=height)

        form = aiohttp.FormData()
        form.add_field("width", "1024")
        form.add_field("image", request_body.image)

        try:
            res = await self.session.post(
                f"/v1/generation/{engine_id}/image-to-image/upscale",
                data=form,
            )
        except ClientResponseError as e:
            raise figure_out_exception(e) from e

        return ImageToImageUpscaleResponseBody.parse_obj(await res.json())

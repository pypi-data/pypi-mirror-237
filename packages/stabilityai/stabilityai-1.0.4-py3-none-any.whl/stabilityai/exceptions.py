import textwrap

from aiohttp.client_exceptions import ClientResponseError


class YouNeedToUseAContextManager(ValueError):
    pass


class ThisFunctionRequiresAPrompt(ValueError):
    pass


class StabilityAiError(Exception):
    retryable: bool = False


class YouAreHoldingItWrong(StabilityAiError):
    pass


class ApiKeyIsMissingOrInvalid(StabilityAiError):
    pass


class ImAfraidICantLetYouDoThat(StabilityAiError):
    pass


class YouBrokeTheirServeres(StabilityAiError):
    retryable: bool = True


class ResourceNotFound(StabilityAiError):
    pass


class RateLimitOrServerError(StabilityAiError):
    retryable: bool = True


def figure_out_exception(e: ClientResponseError) -> StabilityAiError:
    if e.status == 400:
        return YouAreHoldingItWrong(
            textwrap.dedent(
                """\
                Either you specificed some combination of options that their
                server doesn't like or it's a bug in this library. If you 
                think it's the latter open up a bug report on

                https://github.com/estheruary/stabilityai
                """
            )
        )
    elif e.status == 401:
        return ApiKeyIsMissingOrInvalid(
            textwrap.dedent(
                """\
                This could be one of a few problems. If you don't have an API
                key you should generate one at

                  https://beta.dreamstudio.ai/account

                If you have an API key there are two ways to provide it to this
                library. The first and most common is via the environment. You
                to set STABILITY_API_KEY.

                The second method is to provide it to the client constructor
                directly.

                    async with AsyncStabilityClient(api_key="your-key") as stability:
                      ...
                """
            )
        )
    elif e.status == 403:
        return ImAfraidICantLetYouDoThat(
            textwrap.dedent(
                """\
                At the time of writing (Jun 2023) Stability doesn't have any
                permissions on their API so if you get this it's likely
                a bug in this library or a problem on their servers. If you
                think it's the former report it at

                    https://github.com/estheruary/stabilityai
                """
            )
        )
    elif e.status == 429:
        return RateLimitOrServerError(
            textwrap.dedent(
                """\
                Stability's rate limit is 150 req / 10 sec. If you get this
                error on *every* request then it's a bug on their servers.
                You need to generate a new API key and delete the old one.
                """
            )
        )
    elif e.status == 404:
        return ResourceNotFound(
            textwrap.dedent(
                """\
                This usually happens when you specify models that don't exist
                *or* a combination of model/sampler that doesn't work together.
                """
            )
        )
    elif e.status == 500:
        return YouBrokeTheirServeres(
            textwrap.dedent(
                """\
                Impressive. This is not an error you can do anything about
                except retry. Stability might be having an outage or a
                problem on their servers.
                """
            )
        )
    else:
        return StabilityAiError(
            textwrap.dedent(
                """\
                Sorry, I don't know what's up with this error.
                """
            )
        )

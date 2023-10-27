from numbers import Number
from typing import Mapping, Sequence


def serialize_for_form(data, path="", res={}):
    print(data, path, res)
    if isinstance(data, Mapping):
        for key, val in data.items():
            if val is not None:
                xxx = f"{path}[{key}]" if path else key
                serialize_for_form(val, xxx, res)
    elif isinstance(data, Sequence) and not isinstance(data, str):
        for i, elem in enumerate(data):
            serialize_for_form(elem, f"{path}[{i}]", res)
    elif isinstance(data, Number):
        res[path] = str(data)
    else:
        res[path] = data

    return res


if __name__ == "__main__":
    dat = {
        "text_prompts": [{"text": "Birthday party at a gothic church", "weight": None}],
        "init_image": None,
        "init_image_mode": None,
        "image_strength": 0.3,
        "step_schedule_start": None,
        "step_schedule_end": None,
        "cfg_scale": None,
        "clip_guidance_preset": None,
        "sampler": None,
        "sample_extras": None,
    }
    s = serialize_for_form(dat)

    print(s)

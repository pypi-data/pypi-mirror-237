import json
import pathlib

import torch

from music_de_limiter.load_models import load_model_with_args


def load_pretrained_model(device=None):
    if device is not None:
        pass
    elif torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    base_dir = pathlib.Path(__file__).parent.absolute() / "pretrained"

    with open(base_dir / "args.json") as f:
        args = json.load(f)

    model, sample_rate = load_model_with_args(args)

    state_dict = torch.load(base_dir / "weights.pth", map_location=device)
    model.load_state_dict(state_dict)

    return model, sample_rate

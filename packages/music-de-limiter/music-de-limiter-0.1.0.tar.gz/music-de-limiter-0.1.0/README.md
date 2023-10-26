# De-limiter

Derived from [the official repository](https://github.com/jeonchangbin49/De-limiter).

## Usage

### Installation

```sh
$ pip install music-de-limiter
```

or

```sh
$ pip install git+https://github.com/kimagure-humoresque/de-limiter
```

### Usage

```python
import music_de_limiter
import torchaudio
import soundfile as sf

model, sr = music_de_limiter.load_pretrained_model()
wav, _ = torchaudio.sox_effects.apply_effects_file("input.wav", [["rate", "-vsL", f"{sr}"]])
_, result, *_ = model(wav.unsqueeze(0))
sf.write("output.wav", result.squeeze(0).detach().cpu().numpy().T, sr)
```

## License

This repository is licensed under the MIT License.

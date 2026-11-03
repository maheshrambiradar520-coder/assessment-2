# MiniCheck: Efficient Fact-Checking of LLMs on Grounding Documents

Assessment 2 project based on [Liyan06/MiniCheck](https://github.com/Liyan06/MiniCheck).

## Run the demo

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
python run_demo.py
```

The first run downloads the Flan-T5 MiniCheck checkpoint from Hugging Face.

## Expected output

For the included example, the expected labels are `[1, 0]`. The upstream example reports support probabilities around `[0.9806, 0.0071]`. These are reference values, not output observed in this environment.

## Execution status

Inference is pending because the Hugging Face checkpoint download did not progress in this environment. Add a screenshot of a completed run here after inference succeeds.

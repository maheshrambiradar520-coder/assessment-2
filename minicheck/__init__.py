import os

import nltk


_nltk_data_dir = os.environ.get("NLTK_DATA")
if _nltk_data_dir:
    os.makedirs(_nltk_data_dir, exist_ok=True)
    if _nltk_data_dir not in nltk.data.path:
        nltk.data.path.insert(0, _nltk_data_dir)

for _package in ("punkt", "punkt_tab"):
    try:
        nltk.data.find(f"tokenizers/{_package}")
    except LookupError:
        nltk.download(_package, download_dir=_nltk_data_dir, quiet=True)

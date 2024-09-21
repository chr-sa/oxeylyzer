# German corpus

## Discord German Corpus

https://drive.google.com/file/d/1Me-r_K2TFX06dQfWzZ52AQNCikSnADvY/view?usp=sharing

Found this one linked in discord.

## Leipzig Corpus

https://wortschatz.uni-leipzig.de/en/download/German#deu_news_2023

## Snug Parallel Corpus

https://www.statmt.org/europarl/

# Usage

The corpora have to be placed in `./static/text/` as a directory with the name that has to be passed to the `load` command in the repl. Inside this directory there have to be the files containing the corpus.

# Scripts

The `remove_key.py` script was used to generate the ge55, ge46, ... languages. This was done by removing all ngrams containing the deadkey `*` from the german_english50-50, ... languages.

import json
import numpy as np
import matplotlib as plt

with open("./static/language_data/german.json") as f:
    data = json.load(f)


def rank_bigrams(letter, data):
    bigrams = data["bigrams"]
    letter_bigrams = [
        # (bg, freq) for bg, freq in bigrams.items() if bg.startswith(letter)
        (bg, freq)
        for bg, freq in bigrams.items()
        if bg.endswith(letter)
    ]
    letter_bigrams = sorted(letter_bigrams, key=lambda t: t[1], reverse=True)
    for t in letter_bigrams:
        print(t)


if __name__ == "__main__":
    print(rank_bigrams("z", data))

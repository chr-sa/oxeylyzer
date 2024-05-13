import json
from typing import Any


name = "ger-en20-80"
w1 = 0.2
w2 = 0.8

l1_file = "./static/language_data/german_deadkey.json"
l2_file = "./static/language_data/english.json"
target_file = f"./static/language_data/{name}.json"


def sum_frequencies(d: dict[str, float]) -> float:
    return sum(d.values())

def normalize_language_dict(d: dict[str, Any]):
    for k in d:
        if k == "language":
            continue
        freq_dict = d[k]
        s = sum_frequencies(freq_dict)
        d[k] = {bg: freq / s for bg, freq in d[k].items()}
    return d

with open(l1_file, "r") as f:
    l1 = json.load(f)
with open(l2_file, "r") as f:
    l2 = json.load(f)

l1 = normalize_language_dict(l1)
l2 = normalize_language_dict(l2)

combined: dict[str, Any] = dict()
# Combine the corpora.
for ngram_type, frequency_dict in l1.items():
    if ngram_type == "language":  # Each dict contains the language name besides the frequencies.
        continue

    # Fill the combined dict with values from l1 multiplied by the weight for it.
    combined[ngram_type] = {ngram: frequency * w1 for ngram, frequency in frequency_dict.items()}
    for gram, frequency in l2[ngram_type].items():
        try:
            combined[ngram_type][gram] += frequency * w2
        except KeyError:
            combined[ngram_type][gram] = frequency * w2
    
    # Sort according to frequency.
    combined[ngram_type] = {k: v for k, v in sorted(combined[ngram_type].items(), key=lambda item: item[1], reverse=True)}
    print(sum_frequencies(combined[ngram_type]))

combined["language"] = name

with open(target_file, "w") as f:
    json.dump(combined, f, indent=2)

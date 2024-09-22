import matplotlib.pyplot as plt
from pathlib import Path
import json

# IDEA: Add weighted (0.4 maybe) dsfbs.

# file = Path("./static/language_data/german.json")
# file = Path("./static/language_data/english.json")
file = Path("./static/language_data/ge46.json")
alphabet = "abcdefghijklmnopqrstuvwxyz.,;'"

with open(file, "r") as f:
    data = json.load(f)

bigrams = data["bigrams"]

def get_transition_probabilities(bigrams, letter):
    transition_probabilities = {k: v for k, v in bigrams.items() if letter in k}
    d = dict()

    # combine forward and backward probabilities
    for k, v in transition_probabilities.items():
        # sorted_key = "".join(sorted(k))
        sorted_key = k.replace(letter, "")
        d[sorted_key] = d.setdefault(sorted_key, 0) + v

    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return d

fig, axs = plt.subplots(6, 5, figsize=(26, 16))
i = 0
for row in axs:
    for ax in row:
        letter = alphabet[i]
        d = get_transition_probabilities(bigrams, letter)
        ax.bar(d.keys(), d.values())
        ax.set_title(letter)
        i += 1
fig.tight_layout()

# fig, ax = plt.subplots()

# ax.bar(d.keys(), d.values())
plt.savefig("test.png")
# plt.show()

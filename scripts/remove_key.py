import json
from pathlib import Path


file = Path("./static/language_data/ger-en20-80.json")
# file_raw = Path("./static/language_data_raw/ger-en50-50.json")
new_file = Path("./static/language_data/ge28.json")

with open(file, "r") as f:
    data = json.load(f)

for key in ['characters', 'bigrams', 'skipgrams', 'skipgrams2', 'skipgrams3', 'trigrams']:
    data[key] = {k: v for k, v in data[key].items() if not "*" in k}
    s = sum([v for v in data[key].values()])
    data[key] = {k: v / s for k, v in data[key].items()}

with open(new_file, "w") as f:
    json.dump(data, f)


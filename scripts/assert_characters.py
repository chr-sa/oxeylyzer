from pathlib import Path


chars = "abcdefghijklmnopqrstuvwxyz,./'"
root_dir = Path("static/layouts/my_semicolon/")

for file in [f for f in root_dir.glob("*.kb")]:
    with open(file, "r") as f:
        content = f.read()
    for char in chars:
        assert char in content, f"char {char} not in file {file}"

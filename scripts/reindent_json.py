if __name__ == "__main__":
    from argparse import ArgumentParser
    from pathlib import Path
    import json

    parser = ArgumentParser()
    parser.add_argument("--file", "-f", type=Path)
    args = parser.parse_args()

    with open(args.file, "r") as f:
        data = json.load(f)

    with open(args.file, "w") as f:
        json.dump(data, f, indent=2)

from pathlib import Path


def replace_chars(source_chars, target_char, root_dir):
    for layout_file in root_dir.glob("*"):
        with open(layout_file, "r") as f:
            content = f.read()

        # Remove empty files.
        if content == "":
            print(f"Empty file {layout_file}, deleting...")
            layout_file.unlink()
            continue

        # Replace one of the source chars with the target char.
        replaced = False
        for c in source_chars:
            if c in content:
                content = content.replace(c, target_char)
                replaced = True
                break

        # Delete the file if no char to replace was found.
        if not replaced:
            print(f"Did not find char to replace in {layout_file}, skipping...")
            print(content)
            # layout_file.unlink()
            continue

        # Write the new contents to the file.
        with open(layout_file, "w") as f:
            f.write(content)

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser("Replace characters in all layouts in dir.")
    parser.add_argument("--source", "-s", type=str, help="chars to replace")
    parser.add_argument("--dest", "-d", type=str, help="char to use as replacement")
    parser.add_argument("--dir", type=Path, help="root layout dir")

    args = parser.parse_args()

    replace_chars(args.source, args.dest, args.dir)

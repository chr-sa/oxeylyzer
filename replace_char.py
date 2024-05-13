from pathlib import Path

root_dir = Path("./static/layouts/german_deadkey/")
source_chars = "/;"  # Chars to replace, order matters.
target_char = "*"  # The char that replaces.

for layout_file in root_dir.glob("*"):
    with open(layout_file, "r") as f:
        content = f.read()

    # Remove empty files.
    if content == "":
        print(f"Empty file {layout_file}, deleting...")
        layout_file.unlink()
        continue

    # Replace on of the source chars with the target char.
    replaced = False
    for c in source_chars:
        if c in content:
            content = content.replace(c, target_char)
            replaced = True
            break

    # Delete the file if no char to replace was found.
    if not replaced:
        print(f"Did not find char to replace in {layout_file}, deleting...")
        layout_file.unlink()
        continue

    # Write the new contents to the file.
    with open(layout_file, "w") as f:
        f.write(content)

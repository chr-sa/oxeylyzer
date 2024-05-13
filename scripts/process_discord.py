path = "./corpora_raw/deu_mixed-typical_2011_1M-sentences.txt"

with open(path, "r") as f:
    lines = f.readlines()

alphabet = "abcdefghijklmnopqrstuvwxyzäöüß.,?! -'"
alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
alphabet += "0123456789"

cleaned = list()
for line in lines:
    l = line.split("\t")[1].strip()
    to_replace = list()
    for letter in l:
        if letter not in alphabet:
            to_replace.append(letter)
    for letter in to_replace:
        l = l.replace(letter, "")
    l = l.replace("  ", " ")
    l += "\n"
    cleaned.append(l)


with open("./static/text/mygerman/discord.txt", "w") as f:
    f.writelines(cleaned)


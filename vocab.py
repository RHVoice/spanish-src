import re

def fix_vocab(file_path):
    words = []
    fails = 0
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    word_pattern = re.compile(r"^[a-záéíóúüñ]+$")
    for i, line in enumerate(lines, start=1):
        if not line:
            print(f"Error: Empty line at {i}")
            fails += 1
        elif not word_pattern.match(line):
            fails += 1
            print(f"Error: Invalid character in line {i}: '{line.strip()}'")
        else:
            words.append(line)
    with open(f"fixed-{file_path}", "w", encoding="utf-8") as f:
        f.write("".join(words))
    return fails

def sort_vocab(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        words = sorted(set(line.lower().strip() for line in f if line.strip()))
    with open(f"sorted-{input_file}", "w", encoding="utf-8") as f:
        f.write("\n".join(words) + "\n")

#fails = fix_vocab("vocab-extra.txt")
sort_vocab("vocab.txt")
#print("All done with "+str(fails)+" fails.")
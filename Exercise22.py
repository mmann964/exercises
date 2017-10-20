#!/usr/bin/python


def part_one():
    # Easy exercise -- print how many times each name in the file occurs
    fname = "nameslist.txt"

    with open(fname, 'r') as file_name:
        contents = file_name.read()

    lines = contents.split("\n")
    names = {}

    for name in lines:
        if name in names:
            names[name] += 1
        else:
            names[name] = 1

    print names

def part_two():
    # Harder exercise:  parse the file to see how many files in each category
    fname = "Training_01.txt"
    with open(fname, 'r') as file_name:
        contents = file_name.read()

    categories = {}
    lines = contents.split("\n")
    for line in lines:
        parts = line.split("/")
        if len(parts) > 1:
            c = parts[2:len(parts) - 1]
            category = "/".join(c)
            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1
    sorted_keys = sorted(categories.keys())
    for k in sorted_keys:
        print k, categories[k]

if __name__ == "__main__":
    part_one()
    part_two()

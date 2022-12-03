"""
Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
"""

from pathlib import Path


def get_shareditems(lis):
    shareitems = []
    for rucksack in lis:
        comp_a, comp_b = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        for item in set(comp_a):
            if item in comp_b:
                shareitems.append(item)
    return shareitems

def get_priority(char):
    if ord(char) >= 96 and ord(char) <= 122:
        return ord(char) - 96
    if ord(char) >= 65 and ord(char) <= 90:
        return ord(char) - 38

if __name__ == "__main__":
    p = Path(__file__).with_name("day_three_input.txt")
    input_data = open(p).read().splitlines()
    part_one = sum([get_priority(item) for item in get_shareditems(input_data)])
    print(part_one) # ans = 7763
    elf_groups = [input_data[i:i + 3] for i in range(0, len(input_data), 3)]
    badges = ["".join(set(a) & set(b) & set(c)) for a,b,c in elf_groups]
    part_two = sum([get_priority(badge) for badge in badges])
    print(part_two) # ans = 2569

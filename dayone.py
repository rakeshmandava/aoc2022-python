from pathlib import Path

def get_cals(file):
    cals = []
    for elf_calories in open(file).read().split('\n\n'):
        elf_calories = tuple(map(int, elf_calories.split('\n')))
        cals.append(elf_calories)
    return cals

def top_elf(lis):
    return max([sum(items) for items in lis])

def top3_elves(lis):
    lis = sorted([sum(items) for items in lis],reverse = True)
    return lis[0] + lis[1] + lis[2]

if __name__ == "__main__":
    p = Path(__file__).with_name("day_one_input.txt")
    input_data = get_cals(p)
    print(top_elf(input_data)) # ans = 67633
    print(top3_elves(input_data)) #ans = 199628
    
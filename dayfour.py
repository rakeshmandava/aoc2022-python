from pathlib import Path


def get_assignments(lis):
    ids = []
    for pair in lis:
        elf1_task,elf2_task = pair.split(",")
        elf1_lower,elf1_upper = (int(id) for id in elf1_task.split("-"))
        elf2_lower,elf2_upper = (int(id) for id in elf2_task.split("-"))
        elf1_ids = set(i for i in range(elf1_lower,elf1_upper+1))
        elf2_ids = set(i for i in range(elf2_lower,elf2_upper+1))
        ids.append((elf1_ids,elf2_ids))
    return ids

def get_overlaps_count(lis):
    count = 0
    for (elf1,elf2) in lis:
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            count += 1
    return count

def get_partialoverlaps_count(lis):
    count =0
    for (elf1,elf2) in lis:
        if len(elf1.intersection(elf2)) > 0:
            count += 1
    return count



if __name__ == "__main__":
    p = Path(__file__).with_name("day_four_input.txt")
    input_data = open(p).read().splitlines()
    assignments = get_assignments(input_data)
    part_one = get_overlaps_count(assignments)
    print(part_one) # ans = 444
    part_two = get_partialoverlaps_count(assignments)
    print(part_two) # ans = 444

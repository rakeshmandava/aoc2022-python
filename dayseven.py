from pathlib import Path
from collections import defaultdict

def get_dirs_sizes(commands):
    fs = defaultdict(int)
    path = []

    for cmd in commands:
        match cmd.strip().split():
            case ["$", "ls"]:
                continue
            case ["$", "cd", "/"]:
                path = ["/"]
            case ["$", "cd", ".."]:
                path.pop()
            case ["$", "cd", new_dir]:
                path.append(new_dir)
            case ["dir", _]:
                continue
            case [size, _]:
                try:
                    size = int(size)
                except:
                    pass

                for i in range(1, len(path)+1):
                    fs['/'.join(path[:i])] += size

    return fs

if __name__ == "__main__":
    p = Path(__file__).with_name("day_seven_input.txt")
    input_data =  open(p).read().splitlines()
    fs = get_dirs_sizes(input_data)
    max_usable = 70000000 - 30000000
    total_used = fs['/']
    need_to_free = total_used - max_usable
    part_one, part_two = 0, 1e9
    for v in fs.values():
        if v <= 100000:
            part_one += v
        if v >= need_to_free:
            part_two = min(part_two, v)
    print(part_one) # ans = 1583951
    print(part_two) # ans = 214171





    
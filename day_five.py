from pathlib import Path

def get_crates(input):
    num_of_crates = 9
    stacks = [[] for _ in range(num_of_crates)]

    for line in input.splitlines()[:-1]:
        for i,c in enumerate(line[1::4]):
            if not c.isspace():
                stacks[i].append(c)

    for stack in stacks:
        stack.reverse()
    
    return stacks

def get_top_crates(crates,moves):
    for move in moves.splitlines():
        _, num_moves, _, src, _, dst = move.split()
        num_moves, src,dst = int(num_moves), int(src), int(dst)

        for _ in range(num_moves):
            crates[dst - 1].append(crates[src - 1].pop())
    
    return ''.join(crate[-1] if crate else '' for crate in crates)

def fast_arrange(crates,moves):
    for move in moves.splitlines():
        _, num_moves, _, src, _, dst = move.split()
        num_moves, src,dst = int(num_moves), int(src), int(dst)

        bunch_of_crates = crates[src-1][-num_moves:]
        del crates[src-1][-num_moves:]

        crates[dst-1].extend(bunch_of_crates)
    
    return ''.join(crate[-1] if crate else '' for crate in crates)


if __name__ == "__main__":
    p = Path(__file__).with_name("day_five_input.txt")
    input_data = open(p).read()
    crates, moves = input_data.split('\n\n')
    arranged_crates = get_crates(crates)
    top_crates = get_top_crates(arranged_crates,moves)
    print(top_crates) # ans = TGWSMRBPN
    arranged_crates = get_crates(crates)
    top_crates_fast_arranged = fast_arrange(arranged_crates,moves)
    print(top_crates_fast_arranged) # ans = TZLTLWRNF


 
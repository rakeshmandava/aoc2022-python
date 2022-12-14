from pathlib import Path

def is_visible(row,col):

    def is_visible_from_above(row, col):
        for x in range(row-1,-1,-1):
            if grid[x][col] >= grid[row][col]:
                return False
        return True

    def is_visible_from_below(row, col):
        for x in range(row + 1, len(grid)):
            if grid[x][col] >= grid[row][col]:
                return False
        return True

    def is_visible_from_left(row, col):
        for x in range(col-1,-1,-1):
            if grid[row][x] >= grid[row][col]:
                return False
        return True

    def is_visible_from_right(row, col):
        for x in range(col+1,len(grid[row])):
            if grid[row][x] >= grid[row][col]:
                return False
        return True

    return (
        is_visible_from_above(row, col)
        or is_visible_from_right(row, col)
        or is_visible_from_below(row, col)
        or is_visible_from_left(row, col)
    )

def part_1(grid):
    grid_size = len(grid)
    num_visible_trees = grid_size * 2 + (grid_size - 2) * 2

    for row in range(1, grid_size - 1):
        for col in range(1, grid_size - 1):
            num_visible_trees += is_visible(row, col)

    return num_visible_trees


def part_2(grid):
    top_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            k = grid[row][col]
            L = R = U = D = 0
            for x in range(col - 1, -1, -1):
                L += 1
                if grid[row][x] >= k:
                    break
            for x in range(col + 1, len(grid[row])):
                R += 1
                if grid[row][x] >= k:
                    break
            for x in range(row - 1, -1, -1):
                U += 1
                if grid[x][col] >= k:
                    break
            for x in range(row + 1, len(grid)):
                D += 1
                if grid[x][col] >= k:
                    break
            top_score = max(top_score, U * D * L * R)
    return top_score


if __name__ == "__main__":
    p = Path(__file__).with_name("day_eight_input.txt")
    input_data =  open(p).read().splitlines()
    grid = [[int(i) for i in row] for row in input_data]
    print(part_1(grid)) # ans = 1679
    print(part_2(grid)) # ans = 536625

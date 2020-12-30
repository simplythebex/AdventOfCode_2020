with open("/Users/Becca/python_scripts/advent_3_input.txt") as data:
    grid = data.read().splitlines()

max_lines = len(grid)
pattern_width = len(grid[0])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def part_1(map):
    x = 0
    tree_count = 0
    for line in map:
        if line[(x % pattern_width)] == "#":
            tree_count += 1
        x += 3
    return "Tree count is " + str(tree_count)

print(part_1(grid))

def part_2(maps):
    multiplied = 1
    for slope in slopes:
        x = 0
        tree_count = 0
        maps = maps[::slope[1]]
        for map in maps:
            if map[x % pattern_width] == "#":
                tree_count += 1 
            x += slope[0]
        multiplied *= tree_count
    return "Multiplied together, you encounted " + str(multiplied) + " trees."

print(part_2(grid))










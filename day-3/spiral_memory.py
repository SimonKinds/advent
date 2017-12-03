import math

def build_layer(grid_multiplier, start_value, start_x, start_y):
    layer = {start_value: (start_x, start_y)}

    if grid_multiplier == 1:
        return layer

    value = start_value
    x = start_x
    y = start_y
    # up
    for _ in range(grid_multiplier - 2):
        value += 1
        y -= 1
        layer[value] = (x, y)

    # left
    for _ in range(grid_multiplier - 1):
        value += 1
        x -= 1
        layer[value] = (x, y)

    # down
    for _ in range(grid_multiplier - 1):
        value += 1
        y += 1
        layer[value] = (x, y)

    # right
    for _ in range(grid_multiplier - 1):
        value += 1
        x += 1
        layer[value] = (x, y)
    
    return layer


def spiral_memory_distance(squares):
    max_mul = math.ceil(math.sqrt(squares))
    max_mul = max_mul if max_mul % 2 == 1 else max_mul + 1

    grid = {1: (0, 0)}
    for mul in range(3, max_mul + 1, 2):
        prev_value = max(grid.keys())
        prev_pos = grid[prev_value]
        grid.update(build_layer(mul, prev_value + 1, prev_pos[0] + 1, prev_pos[1]))

    return abs(grid[squares][0]) + abs(grid[squares][1])

def get_sum_of_surrounding(x, y, grid):
    val = 0
    val += grid.get((x + 1, y), 0)
    val += grid.get((x + 1, y + 1), 0)
    val += grid.get((x, y + 1), 0)
    val += grid.get((x - 1, y + 1), 0)
    val += grid.get((x - 1, y), 0)
    val += grid.get((x - 1, y - 1), 0)
    val += grid.get((x, y - 1), 0)
    val += grid.get((x + 1, y - 1), 0)
    return val

def build_layer_with_sum(grid, grid_multiplier, start_x, start_y):
    grid[(start_x, start_y)] = get_sum_of_surrounding(start_x, start_y, grid)

    x = start_x
    y = start_y

    # up
    for _ in range(grid_multiplier - 2):
        y -= 1

        grid[(x, y)] = get_sum_of_surrounding(x, y, grid)

    # left
    for _ in range(grid_multiplier - 1):
        x -= 1
        grid[(x, y)] = get_sum_of_surrounding(x, y, grid)

    # down
    for _ in range(grid_multiplier - 1):
        y += 1
        grid[(x, y)] = get_sum_of_surrounding(x, y, grid)

    # right
    for _ in range(grid_multiplier - 1):
        x += 1
        grid[(x, y)] = get_sum_of_surrounding(x, y, grid)
    
    return (x, y)

def spiral_memory_sum(max_sum):
    grid = {}
    grid[(0, 0)] = 1

    mul = 3
    x = 0
    y = 0

    while max(grid.values()) < max_sum:
        x, y = build_layer_with_sum(grid, mul, x + 1, y)
        mul += 2
    
    return sorted(filter(lambda x: x[1] > max_sum, grid.items()), key=lambda x: x[1])[0][1]
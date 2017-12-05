def jump(jump_values,  value_updater=lambda x: x + 1):

    idx = jump_values[0]
    jump_values[0] += 1
    jump_count = 1

    while idx < len(jump_values):
        jump_count += 1
        prev_idx = idx
        idx += jump_values[idx]
        jump_values[prev_idx] = value_updater(jump_values[prev_idx])

    return jump_count

def jump_part_two(jump_values):
    return jump(jump_values, value_updater=lambda x: x + 1 if x < 3 else x - 1)


def jump_from_file(filename, fun=jump):
    with open(filename) as f:
        return fun([int(x) for x in f.readlines()])
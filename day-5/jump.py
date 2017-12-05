def jump(jump_values):

    idx = jump_values[0]
    jump_values[0] += 1
    jump_count = 1

    while idx < len(jump_values):
        jump_count += 1
        prev_idx = idx
        idx += jump_values[idx]
        jump_values[prev_idx] += 1

    return jump_count

def jump_from_file(filename):
    with open(filename) as f:
        return jump([int(x) for x in f.readlines()])
def memory_reallocate(initial_memory_layout):
    """
    Counts the amount of steps required before an infinite loop is detected
    """
    seen = set()
    seen_at = {} 

    layout = initial_memory_layout
    rounds = 0

    while tuple(layout) not in seen:
        seen.add(tuple(layout))
        seen_at[tuple(layout)] = rounds

        # index returns the minimum index with the given value
        max_val = max(layout)
        idx = layout.index(max_val)
        layout[idx] = 0

        for _ in range(0, max_val):
            idx = (idx + 1) % len(layout)
            layout[idx] += 1

        rounds += 1

    return (rounds, rounds - seen_at[tuple(layout)])

def memory_reallocate_from_file(filename):
    with open(filename) as f:
        return memory_reallocate([int(x) for x in f.readline().split()])
def knot_hash_impl(lengths: [int], max_value: int) -> [int]:
    current_pos = 0
    skip_length = 0

    values = list(range(0, max_value + 1))
    for pos_incr in lengths:
        values_copy = values.copy()
        for i in range(0, pos_incr):
            back_value = values_copy[(
                current_pos + pos_incr - 1 - i) % len(values)]
            values[(current_pos + i) % len(values)] = back_value
        current_pos = (current_pos + pos_incr + skip_length) % len(values)
        skip_length += 1

    return values


def knot_hash(lengths: [int], max_value=255) -> int:
    values = knot_hash_impl(lengths, max_value)

    return values[0] * values[1]

def knot_hash_from_file(filename: str) -> int:
    with open(filename) as f:
        return knot_hash([int(length) for length in f.readline().split(',')])

def dense_knot_hash_from_file(filename: str) -> int:
    with open(filename) as f:
        return dense_knot_hash(f.readline().strip())

def dense_knot_hash(hash_input: str) -> int:
    lengths = []
    for char in hash_input:
        lengths.append(ord(char))

    lengths = (lengths + [17, 31, 73, 47, 23]) * 64
    values = knot_hash_impl(lengths, 255)

    xors = []
    for i in range(0, 16):
        xors.append(perform_xor(values[i * 16: (i + 1) * 16]))
    
    return to_hex(xors)
   
def perform_xor(values: [int]) -> int:
    current = values[0]
    for val in values[1:]:
        current ^= val
    return current

def to_hex(values: [int]) -> str:
    return ''.join([format(val, '02x') for val in values])


if __name__ == '__main__':
    print('Part one: {}'.format(knot_hash_from_file('input')))
    print('Part two: {}'.format(dense_knot_hash_from_file('input')))

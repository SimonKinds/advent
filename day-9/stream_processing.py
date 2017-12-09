"""
Stream processing
"""

def iterate_stream(stream: str) -> (int, int):
    """
    :return: (group_score, garbage_count)
    """
    score = 0
    garbage_count = 0
    level = 0
    in_garbage = False
    ignore_next = False

    for char in stream:
        if not ignore_next and in_garbage and char != '!' and char != '>':
            garbage_count += 1
        
        if not ignore_next:
            if char == '<':
                in_garbage = True
            elif char == '>':
                in_garbage = False
            elif char == '!':
                ignore_next = True
                continue

            if not in_garbage:
                if char == '{':
                    level += 1
                    score += level
                if char == '}':
                    level -= 1
    
        ignore_next = False

    return (score, garbage_count)

def score_stream(stream: str) -> int:
    """
    Scores a stream of groups and garbage

    :param stream: A string of groups and garbage

    :return: The scoring
    """
    return iterate_stream(stream)[0]


def count_garbage(stream: str) -> int:
    """
    :return: The amount of characters that's garbage
    """
    return iterate_stream(stream)[1]

def score_stream_from_file(filename: str) -> int:
    with open(filename) as stream:
        return score_stream(stream.readline())

def count_garbage_from_file(filename: str) -> int:
    with open(filename) as stream:
        return count_garbage(stream.readline())
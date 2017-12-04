from collections import Counter

def is_passphrase_valid(passphrase):
    counter = Counter(passphrase.split())
    for word, count in counter.items():
        if count > 1:
            return False
    return True

def is_passphrase_valid_anagram(passphrase):
    counter = Counter([frozenset(Counter(chars)) for chars in list(passphrase.split())])
    for word_counter, count in counter.items():
        if count > 1:
            return False
    return True


def count_valid_phrases_from_file(filename, fun):
    with open(filename) as f:
        return sum([fun(line) for line in f.readlines()])

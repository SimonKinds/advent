import re
import collections

class Disk:
    def __init__(self, name, weight=0, children=[]):
        """
        :param children: List of names of children
        """
        self.name = name
        self.weight = weight
        self.children = children

    def __eq__(self, other):
        if not isinstance(other, Disk):
            return False
        return self.name == other.name \
            and self.weight == other.weight \
            and self.children == other.children

    def __repr__(self):
        return '{} ({}) -> {}'.format(self.name, self.weight, self.children)


def parse_disk(disk_string):
    """
    Parses a string e.g. 
    fwft (72) -> ktlj, cntj, xhth
    into a disk object

    :param line: The string to parse
    """
    matches = re.search('(\w+) \((\d+)\)(?: -> (.+))?', disk_string)
    name = matches.group(1)
    weight = int(matches.group(2))
    children = []
    if matches.group(3):
        children = matches.group(3).split(', ') 
    return Disk(name=name, weight=weight, children=children)

def find_root_name(disks):
    disk_names = set([d.name for d in disks])
    

    for disk in disks:
        disk_names.difference_update(disk.children)

    if disk_names:
        return [name for name in disk_names][0]
    else:
        return None

def find_root(disks):
    name = find_root_name(disks)
    if name:
        return [d for d in disks if d.name == name][0]
    return None

def correct_weight(disks):
    """
    Finds the disk with an incorrect weight, and returns its correct weight
    """
    return correct_weight_recursive(find_root(disks), disks)[1]

def correct_weight_recursive(root, disks):
    name_to_disk = {d.name: d for d in disks} 

    correction = None 
    sums = []
    child_weights = []
    for child in root.children:
        child_sum, child_correction = correct_weight_recursive(name_to_disk[child], disks)
        sums.append(child_sum)
        child_weights.append(name_to_disk[child].weight)

        if child_correction:
            correction = child_correction

    unique_sums = set(sums)
    if len(unique_sums) > 1:
        counter = collections.Counter(sums)
        wrong_sum = None
        correct_sum = None

        for value, count in counter.items():
            if count > 1:
                correct_sum = value
            else:
                wrong_sum = value

        idx = sums.index(wrong_sum)
        sums[idx] = correct_sum
        correction = child_weights[idx] - (wrong_sum -correct_sum)

    return (sum(sums) + root.weight, correction)


def find_root_from_input_file(filename):
    with open(filename) as f:
        return find_root([parse_disk(line) for line in f.readlines()])

def find_correction_from_input_file(filename):
    with open(filename) as f:
        return correct_weight([parse_disk(line) for line in f.readlines()])

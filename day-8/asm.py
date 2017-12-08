import re

def check_cond(a, cond, b, state):
    if cond == '==':
        return state.get(a, 0) == b
    elif cond == '!=':
        return state.get(a, 0) != b
    elif cond == '>':
        return state.get(a, 0) > b
    elif cond == '>=':
        return state.get(a, 0) >= b
    elif cond == '<':
        return state.get(a, 0) < b
    elif cond == '<=':
        return state.get(a, 0) <= b
    else:
        raise RuntimeError('Invalid cond {}'.format(cond))

def perform_op(reg, op_string, op_value, state):
    if op_string == 'inc':
        state[reg] = state.get(reg, 0) + op_value
    elif op_string == 'dec':
        state[reg] = state.get(reg, 0) - op_value
    else:
        raise RuntimeError('Invalid op {}'.format(op_string))
    return state


def evaluate_asm(string, state):
    """
    Evaluates one line of string asm

    :param string: asm in string format
    :param state: The state of the registers
    :return: The new state
    """
    groups = re.search("(\w+) (inc|dec) (-?\d+) if (\w+) (.+) (-?\d+)", string).groups()
    
    reg = groups[0]
    op_string = groups[1]
    op_value = int(groups[2])
    a_cond = groups[3]
    cond_op = groups[4]
    b_cond = int(groups[5])

    if check_cond(a_cond, cond_op, b_cond, state):
        return perform_op(reg, op_string, op_value, state)
    return state
    
def evaluate_multiple_asm(list_of_asm):
    state = {}
    for asm in list_of_asm:
        state = evaluate_asm(asm, state)
    return state

def get_max_during_ops(list_of_asm):
    max_val = None
    state = {}
    for asm in list_of_asm:
        state = evaluate_asm(asm, state)
        values = list(state.values())
        if max_val:
            values.append(max_val)
        max_val = max(values)
    return max_val

def get_max_reg_from_file(filename):
    with open(filename) as f:
        return max(evaluate_multiple_asm(f.readlines()).values())

def get_max_during_ops_from_file(filename):
    with open(filename) as f:
        return get_max_during_ops(f.readlines())

from my_utils.tests import test_and_solve
import numpy as np


DAY_NR = 16


def parse_input(puzzle_input):
    samples, test_program = puzzle_input.split('\n\n\n\n')
    samples = [ss.split('\n') for ss in samples.split('\n\n')]
    samples = [[tuple(eval(ss[0][8:])),
      tuple(int(x) for x in ss[1].split()),
      tuple(eval(ss[2][8:]))]
      for ss in samples]
    return samples, test_program


def addr(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = register[a] + register[b]
    return tuple(register)

def addi(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = register[a] + b
    return tuple(register)

def mulr(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = register[a] * register[b]
    return tuple(register)

def muli(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = register[a] * b
    return tuple(register)

def banr(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = register[a] & register[b]
    return tuple(register)

def bani(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = register[a] & b
    return tuple(register)

def borr(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = register[a] | register[b]
    return tuple(register)

def bori(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = register[a] | b
    return tuple(register)

def setr(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = register[a]
    return tuple(register)

def seti(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = a
    return tuple(register)

def gtir(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = int(a > register[b])
    return tuple(register)

def gtri(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = int(register[a] > b)
    return tuple(register)

def gtrr(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = int(register[a] > register[b])
    return tuple(register)

def eqir(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = int(a == register[b])
    return tuple(register)

def eqri(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = int(register[a] == b)
    return tuple(register)

def eqrr(register, instructions):
    a, b, c = instructions
    register = list(register)
    register[c] = int(register[a] == register[b])
    return tuple(register)


OPCODES = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, 
           gtir, gtri, gtrr, eqir, eqri, eqrr]


def part_1(puzzle_input):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    samples, _ = parse_input(puzzle_input)
    return sum([sum([op(ss[0], ss[1][1:]) == ss[2] for op in OPCODES]) >= 3
                for ss in samples])


def dfs(matches, opcode_dict=None):
    if matches.sum() == 0:
        return
    
    
    
    
def part_2(puzzle_input):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    samples, test_program = parse_input(puzzle_input)
    matches = np.array([[ss[1][0] if op(ss[0], ss[1][1:]) == ss[2] else np.nan
                         for op in OPCODES] for ss in samples])
    candidates = {}
    for col in range(matches.shape[1]):
        x = matches[:, col]
        x = x[np.isfinite(x)]
        candidates[col] = np.unique(x).astype(int).tolist()
    opcode_dict = {}
    # predict depth first search will be quicker (may be just one line)
    while True:
        if sum([len(candidates[key])==1 for key in candidates.keys()]) == 0:
            break
        for key in candidates:
            if len(candidates[key]) == 1:
                code = candidates[key][0]
                opcode_dict[code] = OPCODES[key]
                for key in candidates:
                    if code in candidates[key]:
                        candidates[key].remove(code)
                continue
    # it was one line!
    program = [[int(cc) for cc in line.split()] 
            for line in test_program.split('\n')]
    register = [0, 0, 0, 0]
    for line in program:
        op = opcode_dict[line[0]]
        register = op(register, line[1:])
    return register[0]



if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': [],
        'outputs': []
    }
    test_data2 = {
        'inputs': [],
        'outputs': []
    }
    
    # Code to import the actual puzzle input
    with open(f'./inputs/day_{DAY_NR}.txt') as f:
        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Performs testing and calculates puzzle outputs
    test_and_solve(test_datas=[test_data1, test_data2],
                   functions=[part_1, part_2],
                   puzzle_input=puzzle_input,
                   test_functions=None)

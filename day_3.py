from __future__ import division, print_function
import os
from my_utils.tests import test_function

DAY_NR = 3


def parse_line(line):
    claim_id, rest = line[1:].split('@')
    claim_id = int(claim_id)
    top_corner, size = rest.split(':')
    x1_start, x0_start = [int(x) for x in top_corner.split(',')]
    x1_size, x0_size = [int(x) for x in size.split('x')]
    x1_end, x0_end = x1_start + x1_size-1, x0_start + x0_size-1
    return claim_id, x0_start, x0_end, x1_start, x1_end


def part_1(puzzle_lines):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    claims = set()
    double_claims = set()
    for line in puzzle_lines:
        claim_id, x0_start, x0_end, x1_start, x1_end = parse_line(line)
        for ii in range(x0_start, x0_end+1):
            for jj in range(x1_start, x1_end+1):
                if (ii, jj) not in claims:
                    claims.add((ii, jj))
                else:
                    double_claims.add((ii, jj))
    return len(double_claims)


def part_2(puzzle_lines):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    claims = set()
    double_claims = set()
    for line in puzzle_lines:
        claim_id, x0_start, x0_end, x1_start, x1_end = parse_line(line)
        for ii in range(x0_start, x0_end+1):
            for jj in range(x1_start, x1_end+1):
                if (ii, jj) not in claims:
                    claims.add((ii, jj))
                else:
                    double_claims.add((ii, jj))
    for line in puzzle_lines:
        claim_id, x0_start, x0_end, x1_start, x1_end = parse_line(line)
        for coords in [(ii, jj) for ii in range(x0_start, x0_end+1) 
                        for jj in range(x1_start, x1_end+1)]:
            if coords in double_claims:
                break
        else:
            return claim_id
                    


def main(test_datas, functions, puzzle_input=None, test_functions=None,
         expand=False):
    if test_functions is None:
        test_functions = functions
    for ii, (test_data, fun) in enumerate(zip(test_datas, test_functions)):
        nr_errors = test_function(fun, test_data, expand)
        if nr_errors == 0:
            print('Pt. {} Tests Passed'.format(ii+1))

    if puzzle_input is not None:
        fn = os.path.basename(__file__)
        for ii, fun in enumerate(functions):
            ans = fun(puzzle_input)
            print('{} Pt. {} Solution: {}'.format(fn, ii+1, ans))


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
#        puzzle_input = f.read().strip()
        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1],
         functions=[part_2],
         puzzle_input=puzzle_input,
         test_functions=None)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)

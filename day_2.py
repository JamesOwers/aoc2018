from __future__ import division, print_function
import os
from my_utils.tests import test_function

DAY_NR = 2

def part_1(puzzle_lines):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    nr_twos, nr_threes = 0, 0
    for line in puzzle_lines:
        letter_counts = {}
        for letter in line:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        nr_twos += int(any([ll==2 for ll in letter_counts.values()]))
        nr_threes += int(any([ll==3 for ll in letter_counts.values()]))
    return nr_twos * nr_threes


def part_2(puzzle_lines):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    for ii, line in enumerate(puzzle_lines):
        for line2 in puzzle_lines[ii+1:]:
            nr_diffs = 0
            for jj, letter in enumerate(line):
                if line2[jj] != letter:
                    nr_diffs += 1
                if nr_diffs > 1:
                    break
            if nr_diffs == 1:
                same_letters = []
                for jj, letter in enumerate(line):
                    if line2[jj] == letter:
                        same_letters += [letter]
    return ''.join(same_letters)


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
        'inputs': [['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd',
                    'abcdee', 'ababab']],
        'outputs': [12]
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
#    main(test_datas=[test_data1],
#         functions=[part_1],
#         puzzle_input=puzzle_input,
#         test_functions=None)

    main(test_datas=[],
          functions=[part_2],
          puzzle_input=puzzle_input)

from my_utils.tests import test_and_solve
import numpy as np


DAY_NR = 15


def str_to_array(board_str):
    board = [list(line.strip()) for line in board_str.strip().split('\n')]
    return np.array(board)


def array_to_str(board):
    return '\n'.join([''.join(row) for row in board])


def part_1(puzzle_input, print_delay=None):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    # parse board:
    #     make numpy array
    #     initialise location list of tuples: [(team, location), ...], 
    #     initialise hit points, dict(goblins: dict(location: hp), elves: ...)
    # for each round: decide on an order to progress characters
    # for each character:  # allow mutation of this list - while ii < len(list)
    #     if no enemies: exit
    #     if next to enemy, attack:
    #         pick enemy with fewest hit points (break tie with reading order)
    #         do 3 damage to enemy (all start with 200hp)
    #         if enemy hp <= 0 then they die
    #     else:
    #         get target points (free spaces adjacent to enemies)
    #         get distance to every point on board *if can get there*:
    #             recursively step away from position incrementing counter
    #             if already visited, if counter smaller:
    #                 replace and continue
    #             else: terminate
    #             if move to non '.' also terminate
    #             *dont forget to store first step location too!*
    #         get target point distances, break ties with reading order
    #         move to 'first step location'
    #         if no target points in distances, stay still
    board = str_to_array(puzzle_input)
    print(board)
    if print_delay is not None:
        board_str = array_to_str(board)
        print(board_str, end='\r')
    return None


def part_2(puzzle_input):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    return None



if __name__ == "__main__":
    board = """#######   
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#   
#######
"""
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': [board],
        'outputs': [27730]
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
#                   puzzle_input=puzzle_input,
                   test_functions=None)

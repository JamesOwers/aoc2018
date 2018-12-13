from my_utils.tests import test_and_solve
from collections import defaultdict


DAY_NR = 13


def parse_input(puzzle_input):
    row_nr = 0
    col_nr = 0
    tube_dict = {}
    for char in puzzle_input:
        if char == '\n':
            row_nr += 1
            col_nr = 0
            continue
        tube_dict[(row_nr, col_nr)] = char
        col_nr += 1
    return tube_dict


def find_direction(position, direction, tube_dict):
    perp_direction = (direction[1], direction[0])
    next_position = tuple(a+b for a, b in zip(position, perp_direction))
    if next_position in tube_dict:
        if tube_dict[next_position] == ' ':
            return (-perp_direction[0], -perp_direction[1])
        else:
            return perp_direction
    else:
        raise ValueError()


DIRECTIONS = {
        'v': (1, 0),
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1)
    }


CART_CHARS = {v: k for k, v in DIRECTIONS.items()}


def lrs_to_nsew(lrs, direction):
    lrs_dict = {'l': 0, 'r': 1, 's': 2}
    if direction == (1, 0):  # down
        return [(0, 1), (0, -1), (1, 0)][lrs_dict[lrs]]
    if direction == (-1, 0):  # up
        return [(0, -1), (0, 1), (-1, 0)][lrs_dict[lrs]]
    if direction == (0, 1):  # right
        return [(-1, 0), (1, 0), (0, 1)][lrs_dict[lrs]]
    if direction == (0, -1):  # left
        return [(1, 0), (-1, 0), (0, -1)][lrs_dict[lrs]]


def crossroads_direction(crossroads_number):
    return 'lsr'[crossroads_number % 3]


def show_tracks(tracks):
    track_str = ''
    nr_rows = max([kk[0] for kk in tracks.keys()]) + 1
    nr_cols = max([kk[1] for kk in tracks.keys()]) + 1
    for ii in range(nr_rows):
        for jj in range(nr_cols):
            track_str += tracks[ii, jj]
        track_str += '\n'
    return track_str


def part_1(puzzle_input, max_iters=1000):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    tracks = defaultdict(lambda: ' ')  # only need this for easy n, s, e, w
    puzzle_tracks = parse_input(puzzle_input)
    tracks.update(puzzle_tracks)
    nr_rows = max([kk[0] for kk in tracks.keys()]) + 1
    nr_cols = max([kk[1] for kk in tracks.keys()]) + 1
    carts = {}
    for ii, jj in [(ii, jj) for ii in range(nr_rows) for jj in range(nr_cols)]:
        if tracks[(ii, jj)] in DIRECTIONS:
            carts[(ii, jj)] = {'crossroads': {}, 'prev_char': None}
    for tick in range(max_iters):
        for ii, jj in sorted(carts):
            prev_position = (ii, jj)
            prev_direction = DIRECTIONS[tracks[prev_position]]
            x0_dir, x1_dir = prev_direction
            position = (ii+x0_dir, jj+x1_dir)
            if tracks[position] in DIRECTIONS:
                return f"{position[1]},{position[0]}"
            elif tracks[position] == '+':
                crossroads_dict = carts[prev_position]['crossroads']
                if position not in crossroads_dict:
                    carts[prev_position]['crossroads'][position] = 1
                    turn = 'l'
                else:
                    turn = crossroads_direction(crossroads_dict[position])
                    direction = lrs_to_nsew(turn, prev_direction)
                    carts[prev_position]['crossroads'][position] += 1
            elif tracks[position] in '-|':
                direction = prev_direction
            elif tracks[position] in r'\/':
                direction = find_direction(position, prev_direction, tracks)
            else:
                return "Uh oh"
            
            # update tracks
            n, e, s, w = (ii-1, jj), (ii, jj+1), (ii+1, jj), (ii, jj-1)
            compass_coords = [n, e, s, w]
            compass_chars = [tracks[coord] for coord in compass_coords]
            if carts[prev_position]['prev_char'] is None:
                # assumes no starting on a corner
                if all([char != ' ' for char in compass_chars]):  # xrds
                    prev_char = '+'
                else:
                    if prev_direction[0] == 0:
                        prev_char = '-'
                    else:
                        prev_char = '|'
            else:
                prev_char = carts[prev_position]['prev_char']
            
            new_cart = carts[prev_position]
            new_cart['prev_char'] = tracks[position]
            del carts[prev_position]
            carts[position] = new_cart
            
            tracks[prev_position] = prev_char
            cart_char = CART_CHARS[direction]
            tracks[position] = cart_char
            
            print(f'{tick}, {prev_position}')
            print(show_tracks(tracks))
    return "fail"


def part_2(puzzle_input):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    return None



if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    tracks = r"""/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   
"""
    test_data1 = {
        'inputs': [tracks],
        'outputs': ['7,3']
    }
    test_data2 = {
        'inputs': [],
        'outputs': []
    }
    
    # Code to import the actual puzzle input
    with open(f'./inputs/day_{DAY_NR}.txt') as f:
        puzzle_input = f.read()
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Performs testing and calculates puzzle outputs
    test_and_solve(test_datas=[test_data1, test_data2],
                   functions=[part_1, part_2],
#                   puzzle_input=puzzle_input,
                   test_functions=None)

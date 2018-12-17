from my_utils.tests import test_and_solve
import re
from collections import deque


DAY_NR = 17
FMT1 = re.compile("x=(\d+), y=(\d+)..(\d+)")
FMT2 = re.compile("y=(\d+), x=(\d+)..(\d+)")


def parse_line(line):
    match = FMT1.match(line)
    if match:
        x1_start, x0_start, x0_end = match.groups()
        x1_end = x1_start
    else:
        match = FMT2.match(line)
        if not match:
            print(line)
        x0_start, x1_start, x1_end = match.groups()
        x0_end = x0_start
    clay = [int(x) for x in [x0_start, x0_end, x1_start, x1_end]]
    return [cc + ii for cc, ii in zip(clay, [0, 1, 0, 1])]


def get_scan_str(drips, clay, stagnant, flowing, extent):
    scan_str = ''
    for ii in range(extent[0], extent[1]):
        for jj in range(extent[2], extent[3]):
            pos = (ii, jj)
            if pos in clay:
                scan_str += '#'
            elif pos in stagnant:
                scan_str += '~'
            elif pos in drips:
                scan_str += '*'
            elif pos in flowing:
                scan_str += '|'
            else:
                scan_str += '.'
        scan_str += f'\t{ii}\n'
    return scan_str
                                

def part_1(puzzle_input, print_every=1):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    
    Issue:
Water shouldn't be 'stagnant' if the top is open on one side, but
currently fills to the left with stagnant, which then holds water
like clay
............|....................................|...............
............|....................................|...............
............|....................................|...............    
||||||||||||||||||||||||||||||||||||||||||||||||||...................
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||||||||||||||||....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#|....
|###############################################################|....
    """
    veins = [parse_line(line) for line in puzzle_input]
    x0_min = min([xx for vv in veins for xx in vv[:2]])
    x0_max = max([xx for vv in veins for xx in vv[:2]])
    x1_min = min([xx for vv in veins for xx in vv[2:]])
    x1_max = max([xx for vv in veins for xx in vv[2:]])
    clay = set()
    for vein in veins:
        x0_start, x0_end, x1_start, x1_end = vein
        for ii in range(x0_start, x0_end):
            for jj in range(x1_start, x1_end):
                clay.add((ii, jj))
    everything = clay.copy()
    stagnant = set()
    flowing = set()
    # take from right, append to left
    drips = deque([(0,500)])
    jj = 0
    while len(drips) > 0:
        if print_every is not None:
            if (jj % print_every) == 0:
                print(f"Iteration: {jj}")
                print(get_scan_str(drips, clay, stagnant, flowing,
                                   [x0_min-1, x0_max, 
                                    x1_min-1, x1_max+1]))
                print(drips)
        for ii in range(len(drips)):
            drip = drips.pop()
            below = (drip[0]+1, drip[1])
            left = (drip[0], drip[1]-1)
            right = (drip[0], drip[1]+1)
            if drip[0] == x0_max-1 or (drip[0] == x0_min and drip[1] != 500):
                flowing.add(drip)
                everything.add(drip)
            elif below in flowing:
                flowing.add(drip)
                everything.add(drip)
            elif below not in clay and below not in stagnant:
                drips.appendleft(below)
            elif ((left in everything or left == drips[-1])
                  and (right in everything or right == drips[-1])):
                if left in flowing or right in flowing:
                    flowing.add(drip)
                    everything.add(drip)
#                elif left == drips[-1] or right == drips[-1]:
#                    flowing.add(drip)
#                    everything.add(drip)
                else:
                    stagnant.add(drip)
                    everything.add(drip)
            elif right not in everything and right != drips[-1]:
                drips.appendleft(right)
            elif left not in everything and left != drips[-1]:
                drips.appendleft(left)
            else:
                raise ValueError
        if (1, 500) not in flowing:
            drips.appendleft((0,500))
        jj += 1
    print(f"Iteration: {jj}")
    print(get_scan_str(drips, clay, stagnant, flowing,
                       [x0_min-1, x0_max, 
                        x1_min-1, x1_max+1]))
    return len(flowing) + len(stagnant) - x0_min


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
    test_in= """x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504"""
    test_data1 = {
        'inputs': [test_in.split('\n')],
        'outputs': [57]
    }
    test_data2 = {
        'inputs': [],
        'outputs': []
    }
    
    # Code to import the actual puzzle input
    with open(f'./inputs/day_{DAY_NR}.txt') as f:
#        puzzle_input = f.read().strip()
        puzzle_input = [line.rstrip('\n') for line in f]

    # Performs testing and calculates puzzle outputs
    test_and_solve(test_datas=[test_data1, test_data2],
                   functions=[part_1, part_2],
#                   puzzle_input=puzzle_input,
                   test_functions=None)

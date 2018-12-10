from my_utils.tests import test_and_solve
import re


DAY_NR = 10


def parse_line(line):
    d = "[ \-]?[0-9]+"
    match = re.match(f"position=<({d}), ({d})> velocity=<({d}), ({d})>", line)
    ints = [int(nn) for nn in match.groups()]
    return ints[0:2], ints[2:4]



def part_1(puzzle_input, max_steps=100000, max_letter_height=10):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    lines = [parse_line(line) for line in puzzle_input]
    position, velocity = zip(*lines)
    for step in range(max_steps):
        x0_min = min([pp[0] for pp in position])
        x1_min = min([pp[1] for pp in position])
        x0_max = max([pp[0] for pp in position])
        x1_max = max([pp[1] for pp in position])
        if x1_max - x1_min > max_letter_height:
            position = [[pp[0]+vv[0], pp[1]+vv[1]] for pp, vv 
                    in zip(position, velocity)]
            continue
        else:
            print(f'time = {step}')
            for jj in range(x1_min, x1_max+1):
                for ii in range(x0_min, x0_max+1):
                    if [ii, jj] in position:
                        print('#', end='')
                    else:
                        print('.', end='')
                print()
            position = [[pp[0]+vv[0], pp[1]+vv[1]] for pp, vv 
                        in zip(position, velocity)]
            print()
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
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': ["""position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>""".split('\n')],
        'outputs': ['HI']
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
                   puzzle_input=puzzle_input,
                   test_functions=None)

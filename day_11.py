from my_utils.tests import test_and_solve


DAY_NR = 11


def hundreds(x):
    return (x // 100) % 10


def power(x, y, s):
    return hundreds(x**2*y + 20*x*y + s*x + 100*y + 10*s) - 5


def part_1(puzzle_input):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    serial_number = int(puzzle_input)
    grid = {}
    max_grid_sum = -1000000000
    max_grid_sum_loc = None
    for xx in range(1, 301):  # horizontal
        for yy in range(1, 301):  # vert
            grid[(xx, yy)] = power(xx, yy, serial_number)
            if xx >= 3 and yy >= 3:
                grid_sum = sum([grid[(x, y)] 
                                for x in range(xx, xx-3, -1)
                                for y in range(yy, yy-3, -1)])
                if grid_sum > max_grid_sum:
                    max_grid_sum = grid_sum
                    max_grid_sum_loc = f"{xx-2},{yy-2}"
    return max_grid_sum_loc


def part_2(puzzle_input, max_sz=25):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    serial_number = int(puzzle_input)
    grid = {}
    max_grid_sum = -1000000000
    max_grid_sum_loc = None
    for xx, yy in [(x, y) for x in range(1, 301) for y in range(1, 301)]:
        grid[(xx, yy)] = power(xx, yy, serial_number)
        for sz in range(1, max_sz+1):
            if xx >= sz and yy >= sz:
                grid_sum = sum([grid[(x, y)] 
                                 for x in range(xx, xx-sz, -1)
                                 for y in range(yy, yy-sz, -1)])
                if grid_sum > max_grid_sum:
                    max_grid_sum = grid_sum
                    max_grid_sum_loc = f"{xx-sz+1},{yy-sz+1},{sz}"
    return max_grid_sum_loc



if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': ['18', '42'],
        'outputs': ['33,45', '21,61']
    }
    test_data2 = {
        'inputs': ['18', '42'],
        'outputs': ['90,269,16', '232,251,12']
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

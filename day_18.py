from my_utils.tests import test_and_solve


DAY_NR = 18


def parse_input(puzzle_input):
    chars = list(puzzle_input)
    matrix = {}
    ii = 0
    jj = 0
    for char in chars:
        if char == '\n':
            ii += 1
            jj = 0
            continue
        matrix[(ii, jj)] = char
        jj += 1
    return matrix


def get_neighbours(ii, jj, area, shape):
    coords = [(ii-1, jj-1), (ii-1, jj), (ii-1, jj+1),
              (ii, jj-1), (ii, jj+1),
              (ii+1, jj-1), (ii+1, jj), (ii+1, jj+1)]
    return [area[(x0, x1)] for x0, x1 in coords 
            if x0 >= 0 and x0 < shape[0] and x1 >= 0 and x1 < shape[1]]
             
    
def part_1(puzzle_input, nr_iters=10):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    area = parse_input(puzzle_input)
    shape = [max(x)+1 for x in zip(*area.keys())]
    coords = [(ii, jj) for ii in range(shape[0]) for jj in range(shape[1])]
    for iteration in range(nr_iters):
        prev_area = area.copy()
        # parallelise
        for ii, jj in coords:
            char = area[(ii, jj)]
            neighbours = get_neighbours(ii, jj, prev_area, shape)
            if char == '.':  # open
                if neighbours.count('|') >= 3:
                    area[(ii, jj)] = '|'
            elif char == '|':  # trees
                if neighbours.count('#') >= 3:
                    area[(ii, jj)] = '#'
            elif char== '#':  # lumberyard
                if (neighbours.count('#') >= 1 and 
                    neighbours.count('|') >= 1):
                    area[(ii, jj)] = '#'
                else:
                    area[(ii, jj)] = '.'
    resources = list(area.values())
    value = resources.count('|') * resources.count('#')
    return value


def part_2(puzzle_input, nr_iters=1000):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    area = parse_input(puzzle_input)
    shape = [max(x)+1 for x in zip(*area.keys())]
    coords = [(ii, jj) for ii in range(shape[0]) for jj in range(shape[1])]
    values = []
    for iteration in range(nr_iters):
        resources = list(area.values())
        value = resources.count('|') * resources.count('#')
        values.append(value)
        prev_area = area.copy()
        # parallelise
        for ii, jj in coords:
            char = area[(ii, jj)]
            neighbours = get_neighbours(ii, jj, prev_area, shape)
            if char == '.':  # open
                if neighbours.count('|') >= 3:
                    area[(ii, jj)] = '|'
            elif char == '|':  # trees
                if neighbours.count('#') >= 3:
                    area[(ii, jj)] = '#'
            elif char== '#':  # lumberyard
                if (neighbours.count('#') >= 1 and 
                    neighbours.count('|') >= 1):
                    area[(ii, jj)] = '#'
                else:
                    area[(ii, jj)] = '.'
    resources = list(area.values())
    value = resources.count('|') * resources.count('#')
    values.append(value)
    return values



if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""
    test_data1 = {
        'inputs': [test_data],
        'outputs': [1147]
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

from my_utils.tests import test_and_solve


DAY_NR = 5



def part_1(polymer):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    poly_list = list(polymer)
    ii = 1
    while True:
        if ii >= len(poly_list):
            break
        unit = poly_list[ii]
        anti_unit = unit.upper() if unit == unit.lower() else unit.lower()
        if poly_list[ii-1] == anti_unit:
            del poly_list[ii-1:ii+1]
            ii -= 1
        else:
            ii += 1
#    return ''.join(poly_list)
    return len(poly_list)


def part_2(polymer):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    poly_list = list(polymer)
    units = set([pp.lower() for pp in poly_list])
    smallest_size = part_1(polymer)
    smallest_unit = None
    for unit in units:
        this_poly = ''.join([pp for pp in poly_list 
                             if pp != unit and pp != unit.upper()])
        this_size = part_1(this_poly)
        if this_size < smallest_size:
            smallest_unit = unit
            smallest_size = this_size
    return smallest_size



if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': ['dabAcCaCBAcCcaDA'],
#        'outputs': ['dabCBAcaDA']
        'outputs': [10]
    }
    test_data2 = {
        'inputs': ['dabAcCaCBAcCcaDA'],
        'outputs': [4]
    }
    
    # Code to import the actual puzzle input
    with open(f'./inputs/day_{DAY_NR}.txt') as f:
        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    test_and_solve(test_datas=[test_data1, test_data2],
                   functions=[part_1, part_2],
                   puzzle_input=puzzle_input,
                   test_functions=None)

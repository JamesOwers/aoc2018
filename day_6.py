from my_utils.tests import test_and_solve


DAY_NR = 6


def part_1(puzzle_input):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    coords = [tuple(int(xx) for xx in ss.split(', ')) 
              for ss in puzzle_input]
    (x0_min, x0_max), (x1_min, x1_max) = [(min(xx), max(xx))
                                          for xx in list(zip(*coords))]
    nr_closest = [0] * len(coords)
    inf_list = set()
    for ii in range(x0_min-1, x0_max+2):
        for jj in range(x1_min-1, x1_max+2):
            if ii in (x0_min-1, x0_max+1) or jj in (x1_min-1, x1_max+1):
                distances = [abs(x0-ii) + abs(x1-jj) for x0, x1 in coords]
                min_dist = min(distances)
                idx = distances.index(min_dist)
                inf_list.add(idx)
            else:
                # def inefficient to recalc each time...
                distances = [abs(x0-ii) + abs(x1-jj) for x0, x1 in coords]
                min_dist = min(distances)
                if distances.count(min_dist) == 1:
                    idx = distances.index(min_dist)
                    nr_closest[idx] += 1
    non_inf_closest = [nr_closest[ii] if ii not in inf_list else 0 
                       for ii in range(len(coords))]
    return max(non_inf_closest)

def part_2(puzzle_input, max_dist=10000):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    coords = [tuple(int(xx) for xx in ss.split(', ')) 
              for ss in puzzle_input]
    (x0_min, x0_max), (x1_min, x1_max) = [(min(xx), max(xx))
                                          for xx in list(zip(*coords))]
    regions = []
    for ii in range(x0_min, x0_max+1):
        for jj in range(x1_min, x1_max+1):
            distances = [abs(x0-ii) + abs(x1-jj) for x0, x1 in coords]
            tot = sum(distances)
            if tot < max_dist:
                regions.append(1)
            else:
                regions.append(0)
    # assumes there is only one region
    return sum(regions)



if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': [['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']],
        'outputs': [17]
    }
    test_data2 = {
        'inputs': [['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']],
        'outputs': [16]
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

from my_utils.tests import test_and_solve
from collections import defaultdict


DAY_NR = 12


def trim_state(state, nr_empties=5):
    first_full = state.index('#')
    last_full = state[::-1].index('#')
    first_idx = 0
    if first_full >= nr_empties:
        first_idx = (first_full-nr_empties)
        state = state[first_idx:]
    else:
        first_idx -= (nr_empties-first_full)
        state = '.'*(- first_idx) + state
    if last_full >= nr_empties:
        state = state[:-(last_full-nr_empties+1)]
    else:
        state = state + '.'*(nr_empties-last_full)
    return first_idx, state


def part_1(rules, state, nr_generations=117):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    first_idx = 0
    prev_tot = 0
    print(sum([idx if state=='#' else 0 for idx, state in 
                zip(range(first_idx, first_idx+len(state)), state)]))
    for ii in range(nr_generations):
#        print(ii, state, trim_state(state))
        idx_change, state = trim_state(state)
        first_idx += idx_change
        new_state = []
        for jj in range(len(state)-4):
#            print(state[jj:jj+5], rules[state[jj:jj+5]])
            new_state.append(rules[state[jj:jj+5]])
        state = ''.join(new_state)
        first_idx += 2
        tot = sum([idx if state=='#' else 0 for idx, state in 
                zip(range(first_idx, first_idx+len(state)), state)])
        print(ii, tot - prev_tot)
        prev_tot = tot
    return sum([idx if state=='#' else 0 for idx, state in 
                zip(range(first_idx, first_idx+len(state)), state)])


def part_2(rules, state, nr_generations=20):
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
    rules = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #""".split('\n')
    rules = [rr.split(' => ') for rr in rules]
    new_rules = defaultdict(lambda: '.')
    new_rules.update(rules)
    test_data1 = {
        'inputs': [[new_rules, '#..#.#..##......###...###']],
        'outputs': [325]
    }
    test_data2 = {
        'inputs': [],
        'outputs': []
    }
    
    # Code to import the actual puzzle input
    with open(f'./inputs/day_{DAY_NR}.txt') as f:
#        puzzle_input = f.read().strip()
        puzzle_input = [line.rstrip('\n') for line in f]
        state = puzzle_input[0].split('initial state: ')[1]
        rules = dict([rr.split(' => ') for rr in puzzle_input[2:]])
    # Performs testing and calculates puzzle outputs
    test_and_solve(test_datas=[test_data1, test_data2],
                   functions=[part_1, part_2],
                   puzzle_input=[rules, state],
                   test_functions=None,
                   expand=True)

# 10317 + (50000000000 - 117) * 73
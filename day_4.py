from my_utils.tests import test_and_solve
import re

DAY_NR = 4


def parse_line(puzzle_line):
    match = re.match("\[(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2})\] (.*)",
                     puzzle_line)
    return [int(grp) for grp in match.groups()[:-1]] + [match.groups()[-1]]


def part_1(puzzle_input):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    records =  sorted([parse_line(line) for line in puzzle_input],
                       key=lambda x: x[:-1])
    # Assuming that there is always a 'wakes up' after 'falls asleep'
    # Assuming that 'falls asleep' always comes first after Guard begins
    # Assuming it's possible for guard to not fall asleep, or sleep arbitrary
    # nr of times
    # Assuming all the 
    # N.B. asleep on first minute awake on last minute
    guard_sleeps = {}
    guard_nr, start_sleep, end_sleep = None, None, None
    for rr in records:
        guard_match = re.match("Guard #(\d+) begins shift", rr[-1])
        if guard_match:
            guard_nr = int(guard_match.group(1))
            start_sleep = None
            end_sleep = None
            if guard_nr not in guard_sleeps:
                guard_sleeps[guard_nr] = [0] * 60
        elif "falls asleep" in rr[-1]:
            start_sleep = rr[4]  # the minute
        elif "wakes up" in rr[-1]:
            end_sleep = rr[4]  # the minute
            guard_sleeps[guard_nr][start_sleep:end_sleep] = \
                [xx+1 for xx in guard_sleeps[guard_nr][start_sleep:end_sleep]]
        else:
            NotImplementedError()
    guard_sleep_time = {k: sum(v) for k, v in guard_sleeps.items()}
    sleepiest_guard = max(guard_sleep_time.keys(),
                          key=lambda kk: guard_sleep_time[kk])
    sguard_sleep = guard_sleeps[sleepiest_guard]
    idx = sguard_sleep.index(max(sguard_sleep))
    return sleepiest_guard * idx


def part_2(puzzle_input):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    records =  sorted([parse_line(line) for line in puzzle_input],
                       key=lambda x: x[:-1])
    guard_sleeps = {}
    guard_nr, start_sleep, end_sleep = None, None, None
    for rr in records:
        guard_match = re.match("Guard #(\d+) begins shift", rr[-1])
        if guard_match:
            guard_nr = int(guard_match.group(1))
            start_sleep = None
            end_sleep = None
            if guard_nr not in guard_sleeps:
                guard_sleeps[guard_nr] = [0] * 60
        elif "falls asleep" in rr[-1]:
            start_sleep = rr[4]  # the minute
        elif "wakes up" in rr[-1]:
            end_sleep = rr[4]  # the minute
            guard_sleeps[guard_nr][start_sleep:end_sleep] = \
                [xx+1 for xx in guard_sleeps[guard_nr][start_sleep:end_sleep]]
        else:
            NotImplementedError()
    guard_max_minute = {k: max(v) for k, v in guard_sleeps.items()}
    sleepiest_guard = max(guard_max_minute.keys(),
                          key=lambda kk: guard_max_minute[kk])
    sguard_sleep = guard_sleeps[sleepiest_guard]
    idx = sguard_sleep.index(max(sguard_sleep))
    return sleepiest_guard * idx



if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': [],
        'outputs': []
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
    test_and_solve(test_datas=[test_data1],
                   functions=[part_1, part_2],
                   puzzle_input=puzzle_input,
                   test_functions=None)
    
    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)

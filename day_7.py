from my_utils.tests import test_and_solve
import re
from string import ascii_uppercase


DAY_NR = 7


def parse_line(puzzle_input):
    match_str = "Step ([A-Z]) must be finished before step ([A-Z]) can begin."
    match = re.match(match_str, puzzle_input)
    return match.groups()


def part_1(puzzle_input):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    relations = [parse_line(ll) for ll in puzzle_input]
    all_steps = set()
    dependency_dict = {}
    for b, a in relations:
        all_steps.add(a)
        all_steps.add(b)
        if a not in dependency_dict:
            dependency_dict[a] = [b]
        else:
            dependency_dict[a].append(b)
    queue = []
    for step in all_steps:
        if step not in dependency_dict:
            queue.append(step)
    done = []
    while len(queue) > 0:
        queue.sort()
        task = queue.pop(0)
        done.append(task)
        for kk in list(dependency_dict.keys()):
            if task in dependency_dict[kk]:
                dependency_dict[kk].remove(task)
                if len(dependency_dict[kk]) == 0:
                    queue.append(kk)
                    del dependency_dict[kk]
    return ''.join(done)


def part_2(puzzle_input, nr_workers=5, penalty=60):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    
    relations = [parse_line(ll) for ll in puzzle_input]
    all_steps = set()
    dependency_dict = {}
    for b, a in relations:
        all_steps.add(a)
        all_steps.add(b)
        if a not in dependency_dict:
            dependency_dict[a] = [b]
        else:
            dependency_dict[a].append(b)
    queue = []
    for step in all_steps:
        if step not in dependency_dict:
            queue.append(step)
    workers = [None] * nr_workers
    time = 0
    while len(dependency_dict) > 0 or not all([ww is None for ww in workers]):
#        print(time, workers)
        for ii, worker in enumerate(workers):
            if worker is not None:
                task, task_finish = worker
                if task_finish == time:
                    workers[ii] = None
                    for kk in list(dependency_dict.keys()):
                        if task in dependency_dict[kk]:
                            dependency_dict[kk].remove(task)
                            if len(dependency_dict[kk]) == 0:
                                queue.append(kk)
                                del dependency_dict[kk]
        queue.sort()
        while None in workers and len(queue) > 0:
            worker = workers.index(None)
            task = queue.pop(0)
            task_finish = time + penalty + ascii_uppercase.index(task) + 1
            workers[worker] = (task, task_finish)
        time += 1  
    return time - 1



if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_in = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""
    test_data1 = {
        'inputs': [test_in.split('\n')],
        'outputs': ['CABDFE']
    }
    test_data2 = {
        'inputs': [test_in.split('\n')],
        'outputs': [15]
    }
    
    # Code to import the actual puzzle input
    with open(f'./inputs/day_{DAY_NR}.txt') as f:
#        puzzle_input = f.read().strip()
        puzzle_input = [line.rstrip('\n') for line in f]

    # Performs testing and calculates puzzle outputs
    test_and_solve(test_datas=[test_data1, test_data2],
                   functions=[part_1, part_2],
                   puzzle_input=puzzle_input,
                   test_functions=[part_1, lambda x: part_2(x, nr_workers=2, 
                                                            penalty=0)])

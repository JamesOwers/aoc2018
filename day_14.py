from my_utils.tests import test_and_solve


DAY_NR = 14


class DoublyLinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
    
    def insert_after(self, prev_node):
        next_node = prev_node.next_node
        next_node.prev_node = self
        prev_node.next_node = self
        self.prev_node = prev_node
        self.next_node = next_node
    
    def pop(self):
        self.prev_node.next_node = self.next_node
        self.next_node.prev_node = self.prev_node
        return self.value, self.next_node
    
    def print_list(self, max_print=20):
        print(self.value, end='')
        node = self.next_node
        nr_print = 1
        while node is not self and nr_print <= max_print:
            print(f", {node.value}", end='')
            node = node.next_node
            nr_print += 1
        print()


def part_1(puzzle_input):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    puzzle_input = int(puzzle_input)
    recipe_scores = [3, 7]
    elf_1 = 0
    elf_2 = 1
    while len(recipe_scores) < (puzzle_input + 10):
        score_sum = recipe_scores[elf_1] + recipe_scores[elf_2]
        if score_sum >= 10:
            recipe_scores.append(1)
            recipe_scores.append(score_sum % 10)
        else:
            recipe_scores.append(score_sum)
        elf_1 = (elf_1 + recipe_scores[elf_1] + 1) % len(recipe_scores)
        elf_2 = (elf_2 + recipe_scores[elf_2] + 1) % len(recipe_scores)
    return ''.join([f'{n}' for n in 
                    recipe_scores[puzzle_input:puzzle_input+10]])


def check_match(puzzle_input, match_idx, check):
    if puzzle_input[match_idx] == check:
        match_idx += 1
    else:
        if puzzle_input[0] == check:
            match_idx = 1
        else:
            match_idx = 0
    return match_idx
    

def part_2(puzzle_input):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    puzzle_input = [int(pp) for pp in list(puzzle_input)]
    N = len(puzzle_input)
    recipe_scores = [3, 7]
    elf_1 = 0
    elf_2 = 1
    match_idx = 0
    while True:
        score_sum = recipe_scores[elf_1] + recipe_scores[elf_2]
        if score_sum >= 10:
            recipe_scores.append(1)
            match_idx = check_match(puzzle_input, match_idx, 1)
            if match_idx == N:
                return len(recipe_scores) - len(puzzle_input)
            recipe_scores.append(score_sum % 10)
            match_idx = check_match(puzzle_input, match_idx, score_sum % 10)
        else:
            recipe_scores.append(score_sum)
            match_idx = check_match(puzzle_input, match_idx, score_sum)
        if match_idx == N:
            return len(recipe_scores) - len(puzzle_input)
        elf_1 = (elf_1 + recipe_scores[elf_1] + 1) % len(recipe_scores)
        elf_2 = (elf_2 + recipe_scores[elf_2] + 1) % len(recipe_scores)
    




if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': ['9', 
                   5, 18, 2018
                   ],
        'outputs': ['5158916779', 
                    '0124515891', '9251071085', '5941429882'
                    ]
    }
    test_data2 = {
        'inputs': ['01245', 
                   '51589', '92510', '59414'
                   ],
        'outputs': [5, 
                    9, 18, 2018
                    ]
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

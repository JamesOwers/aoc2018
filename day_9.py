from my_utils.tests import test_and_solve
import re


DAY_NR = 9


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


def parse_input(puzzle_input):
    match = re.match("(\d+) players; last marble is worth (\d+) points",
                     puzzle_input)
    nr_players, nr_marbles = match.groups()
    return int(nr_players), int(nr_marbles)


def part_1(puzzle_input):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    nr_players, nr_marbles = parse_input(puzzle_input)
    pos = 0
    circle = [0]
    scores = [0] * nr_players
    for marble in range(1, nr_marbles+1):
        if marble % 23 != 0: 
            pos = (pos + 2) % len(circle)
            if pos == 0:  # this just makes it convention to keep 0 @ start
                pos = len(circle) 
            circle.insert(pos, marble)
        else:
            curr_player = marble % nr_players
            scores[curr_player] += marble
            pos = (pos - 7) % len(circle)
            scores[curr_player] += circle.pop(pos)
    return max(scores)


def part_1b(puzzle_input):
    nr_players, nr_marbles = parse_input(puzzle_input)
    current_marble = DoublyLinkedListNode(0)
#    first_node = current_marble
    current_marble.next_node = current_marble
    current_marble.prev_node = current_marble
    scores = [0] * nr_players
    for marble in range(1, nr_marbles+1):
#        print(f"Before marble: {marble}, current_marble: {current_marble.value}")
#        first_node.print_list()
        if marble % 23 != 0:
            this_marble = DoublyLinkedListNode(marble)
            this_marble.insert_after(current_marble.next_node)
            current_marble = this_marble
        else:
            curr_player = marble % nr_players
            scores[curr_player] += marble
            for ii in range(7):
                current_marble = current_marble.prev_node
            value, current_marble = current_marble.pop()
            scores[curr_player] += value
    return max(scores)


def part_2(puzzle_input):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    nr_players, nr_marbles = parse_input(puzzle_input)
    nr_marbles *= 100
    puzzle_string= (f"{nr_players} players; last marble is worth {nr_marbles}"
                    " points")
    return part_1b(puzzle_string)



if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': ['9 players; last marble is worth 25 points',
                   '10 players; last marble is worth 1618 points',
                   '13 players; last marble is worth 7999 points',
                   '17 players; last marble is worth 1104 points',
                   '21 players; last marble is worth 6111 points',
                   '30 players; last marble is worth 5807 points'
                  ],
        'outputs': [32, 
#                    8317, 146373, 2764, 54718, 37305
                    ]
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
                   functions=[part_1b, part_2],
                   puzzle_input=puzzle_input,
                   test_functions=None)

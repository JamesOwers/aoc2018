from my_utils.tests import test_and_solve


DAY_NR = 8
 

class Node:
    def __init__(self, metadata=None, children=None):
        self.metadata = metadata
        self.children = children
    
    def add_child(self, node):
        if self.children is None:
            self.children = [node]
        else:
            self.children.append(node)
    
    def add_meta(self, meta):
        if self.metadata is None:
            self.metadata = [meta]
        else:
            self.metadata.append(meta)


def part_1(puzzle_input):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    nr_list = [int(ii) for ii in puzzle_input.split()]
    node_stack = []
    ii = 0
    tot = 0
    while ii < len(nr_list):
        if len(node_stack) != 0:
            nr_children, nr_meta = node_stack[-1]
            if nr_children == 0:
                del node_stack[-1]
            else:
                node_stack[-1] = (nr_children-1, nr_meta)
                nr_children, nr_meta = nr_list[ii:ii+2]
                ii += 2
        else:
            nr_children, nr_meta = nr_list[ii:ii+2]
            ii += 2
        if nr_children == 0:
            for jj in range(nr_meta):
                tot += nr_list[ii]
                ii += 1
        else:
            node_stack += [(nr_children, nr_meta)]
    return tot


def part_2(puzzle_input):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    root_node = build_tree(puzzle_input)
    return node_value(root_node)


def build_tree(puzzle_input):
    nr_list = [int(ii) for ii in puzzle_input.split()]
    root_node = Node()
    node_stack = [(nr_list[0], nr_list[1], root_node)]
    ii = 2
    while ii < len(nr_list):
        nr_children, nr_meta, parent_node = node_stack[-1]
        if nr_children == 0:
            del node_stack[-1]
            this_node = parent_node
        else:
            node_stack[-1] = (nr_children-1, nr_meta, parent_node)
            this_node = Node()
            parent_node.add_child(this_node)
            nr_children, nr_meta = nr_list[ii:ii+2]
            ii += 2
        if nr_children == 0:
            for jj in range(nr_meta):
                this_node.add_meta(nr_list[ii])
                ii += 1
        else:
            node_stack += [(nr_children, nr_meta, this_node)]
    return root_node


def print_tree(node):
    if node.children is None:
        return node.metadata
    else:
        return node.metadata, [print_tree(child) for child in node.children]
            

def node_value(node):
    if node.children is None:
        return sum(node.metadata)
    else:
        return sum([node_value(node.children[idx-1]) for idx in node.metadata
                    if idx <= len(node.children)])

if __name__ == "__main__":
    # Testing data: 
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': ['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'],
        'outputs': [138]
    }
    test_data2 = {
        'inputs': ['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'],
        'outputs': [66]
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

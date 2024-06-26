import copy


class node:
    def __init__(self, value, colour, left, right, parent):
        self.value = value
        self.colour = colour
        self.left = left
        self.right = right
        self.parent = parent

def change_colour(colour):
    if colour == 'B':
        return 'R'
    else:
        return 'B'

def recolour_nodes(current_parent):
    print("Action: recolour")
    global root_node

    if current_parent.parent != root_node:
        current_parent.parent.colour = change_colour(current_parent.parent.colour)
    
    current_parent.parent.left.colour = change_colour(current_parent.parent.left.colour)
    current_parent.parent.right.colour = change_colour(current_parent.parent.right.colour)

def check_conflict(node, node_parent, case):
    if node_parent.colour == 'R':
        print("\nR-R conflict!")
        recolour_nodes(node_parent)
    else:
        print("\nNo conflict!")
    
def insert_node(value):
    global root_node
    current_parent = root_node
    current_value = value
    parent_found = False
    
    while not parent_found: # traverse to get the parent node for current value, then insert
        if current_value < current_parent.value:
            if current_parent.left is None:
                new_node = node(current_value, 'R', None, None, current_parent)
                current_parent.left = new_node # inserted new node
                parent_found = True

                # after insertion, handle R-R conflict if any
                check_conflict(new_node, current_parent, 'normal')

            else:
                current_parent = current_parent.left

        else:
            if current_parent.right is None:
                new_node = node(current_value, 'R', None, None, current_parent)
                current_parent.right = new_node # inserted new node 
                parent_found = True

                # after insertion, handle R-R conflict if any
                check_conflict(new_node, current_parent, 'normal')

            else:
                current_parent = current_parent.right 

    return root_node

def print_tree(node, indent=0, prefix="root"):
    if indent == 0:
        print()
    if node is not None:
        print("|" * indent + "--" * indent + f"{'' if indent == 0 else ' '}" + f"{prefix}: {node.value} {node.colour}")
        print_tree(node.left, indent + 1, "left")
        print_tree(node.right, indent + 1, "right")

input_values = [55,66,27,19,51,83,57,72]
root_node = node(input_values[0], 'B', None, None, None)
print_tree(root_node)
for i in range(1, len(input_values)):
    root_node = insert_node(input_values[i])
    print_tree(root_node)

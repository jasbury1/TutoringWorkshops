class treeNode:
    def __init__(self, value, left, right):
        self.value = value  # Defined to be a positive number
        self.left = left    # Defined to be a treeNode, or None 
        self.right = right  # Defined to be a treeNode, or None

def find_max_in_tree(tree):
    # Given a treeNode, function recursively searches a tree and returns the
    # maximum value in the whole tree

    # Base Case
    if tree == None:
        return -1

    # Reductions of tree into 2 subtrees
    left_tree_max_value = find_max_in_tree(tree.left)
    right_tree_max_value = find_max_in_tree(tree.right)

    # Combining values obtained from recursion
    combined_left_and_right = max(left_tree_max_value, right_tree_max_value)
    combined_total_result = max(combined_left_and_right, tree.value)

    # returning combined values
    return combined_total_result


if __name__ == "__main__":
    # Tree Creation
    tree = treeNode(7, 
        treeNode(6, 
            treeNode(5, 
                treeNode(2, 
                    None,
                    None),
                None
            ),
            treeNode(8,
                None,
                None
            )
        ), 
        treeNode(1,
            None,
            treeNode(4,
                None,
                None
            )
        )
    )

    # Basic tree tests
    print(find_max_in_tree(tree.left))
    print(find_max_in_tree(tree.right))
    print(find_max_in_tree(tree))
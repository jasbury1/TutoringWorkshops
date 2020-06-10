class treeNode:
    def __init__(self, value, left, right):
        self.value = value  # Defined to be a positive number
        self.left = left    # Defined to be a treeNode, or None 
        self.right = right  # Defined to be a treeNode, or None

def find_max_in_tree(tree):
    # Given a treeNode, function recursively searches a tree and returns the
    # maximum value in the whole tree
    pass

if __name__ == "__main__":
    # Tree creation 
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

    # Basic Tree tests
    print(find_max_in_tree(tree.left))
    print(find_max_in_tree(tree.right))
    print(find_max_in_tree(tree))
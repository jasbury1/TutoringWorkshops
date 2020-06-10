# The FamilyTreeNode must:
#   - Have it's own name representing the person at the node of the tree
#   - Have any number of children which are also FamilyTreeNodes. (hint: try a
#     List of FamilyTreeNodes)
#   - Have an init function which initializes the values described above
#   - Have a repr function which simply returns the FamilyTreeNode name.
#
# get_children must:
#   - Use recursion to go back numGenerations number of generations and return
#     all of the children from that generation. (i.e. if you pass in 2 for
#     numGeneration, you have to return all of the grandchildren of the passed
#     in FamilyTreeNode)
#   - Take into account all of the children of the FamilyTreeNode
#   - return a List of FamilyTreeNode that are numGenerations separated
#   - return an empty list if reaches a leaf node (no children)

class FamilyTreeNode:
    def __init__(self):
        pass
    def __repr__(self):
        pass

def get_children(family_tree, numGenerations):
    # Given a FamilyTreeNode and a number representing number of generations to
    # go back, function returns a list of FamilyTreeNodes representing the
    # numGenerations back of the family_tree node.
    pass

if __name__ == "__main__":
    # Creating Family Tree here
    
    # Example tests for the get_children function
    print(get_children(parent, 2))
    print(get_children(grandchild2, 2))
    print(get_children(child1, 1))
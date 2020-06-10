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
    def __init__(self, name, children):
        self.name = name            # Defined to be a positive number
        self.children = children    # Defined to be a list of FamilyTreeNodes
                                    # or an empty list if no children
    def __repr__(self):
        return str(self.name)

def get_children(family_tree, numGenerations):
    # Given a FamilyTreeNode and a number representing number of generations to
    # go back, function returns a list of FamilyTreeNodes representing the
    # numGenerations back of the family_tree node.

    # Base Cases
    if family_tree is None:
        return []
    if numGenerations == 1:
        return family_tree.children
    if numGenerations < 1:
        return family_tree

    combined_children = []

    # Reduction and combination i - total reductions = number of children
    for child in family_tree.children:
        # Reduction i - break into per child tree
        children = get_children(child, numGenerations - 1)
        # Combination i - combine array into unified array
        combined_children += children

    # Return combined results
    return combined_children

if __name__ == "__main__":
    # Creating Family Tree
    grandchild1 = FamilyTreeNode("grandchild1", [])
    grandchild2 = FamilyTreeNode("grandchild2", [])
    grandchild3 = FamilyTreeNode("grandchild3", [])
    grandchild4 = FamilyTreeNode("grandchild4", [])

    child1 = FamilyTreeNode("child1", [grandchild1, grandchild3, grandchild4])
    child2 = FamilyTreeNode("child2", [grandchild2])
    child3 = FamilyTreeNode("child3", [])

    parent = FamilyTreeNode("parent", [child1, child2, child3])

    # Testing get_children function
    print(get_children(parent, 2))
    print(get_children(grandchild2, 2))
    print(get_children(child1, 1))
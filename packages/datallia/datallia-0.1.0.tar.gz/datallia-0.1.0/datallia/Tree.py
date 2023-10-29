class TreeNode:
    def __init__(self, data):
        self.data = data # actual data to be stored inside the node
        self.children = [] # list for the children

    # simple function to add a child given the data
    def add_child(self, data):
        child_node = TreeNode(data) # create child node with the data given
        self.children.append(child_node) #add child by appending it


    # simple function to add a child given the node
    def add_childNode(self, child_node):
        self.children.append(child_node) # add child by appending it

    # simple function to add a parent to an orphan node
    def add_Parent(self, parent_node):
        parent_node.add_childNode(self) # add parent to the node by appending it to the intended parent children

    # simple function to get the heigh of a node
    def height(self):
        if not self.children: # if no children height is zero
            return 0
        else:
            heights = [child.height() for child in self.children] # construc list of children heights
            return 1 + max(heights) # return highest height of children

    def __repr__(self, level=0):
        ret = "\t" * (level) + repr(self.data)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

class Tree:
    def __init__(self, root):
        self.root = root

    def height(self):
        return height(self.root)

    def __repr__(self):
        print(self.root)
from avl import AVLTree, comp_1
from object import Object, Color
class Bin:
    def __init__(self, bin_id, capacity):
        self.remcapacity=capacity
        self.bin_id=bin_id
        self.objectTree=AVLTree()
        

    def add_object(self, object):
        # Implement logic to add an object to this bin
        # if object.size < self.remcapacity:
           

            self.objectTree.insert(object.object_id,object.size)
            # print(self.objectTree.inorder(self.objectTree.root))
            self.remcapacity=self.remcapacity-object.size
            object.binid=self.bin_id
        # print("sahi hai")

        

    def remove_object(self, object):
        # Implement logic to remove an object by ID
        self.objectTree.remove(object.object_id)
        self.remcapacity=self.remcapacity+object.size

    
    
    def getobj(self):

        return self.objectTree.inorder(self.objectTree.root)  #self.treeobj.root



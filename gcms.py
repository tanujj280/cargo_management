from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.tree1=AVLTree()
        self.tree2=AVLTree()
        self.treeobj=AVLTree()
        

    def add_bin(self, bin_id, capacity):
        p=Bin(bin_id,capacity)
        
        self.tree1.insert(bin_id,p)
        self.tree2.insert((capacity,bin_id),p)
       
    
        
        
       
       

    
    # def suitable_bin(self, size, color):
    #     ro = self.tree2.root

    #     if color == Color.BLUE:
    #         curr = ro
    #         # Compact fit: smallest ID
    #         small = None
    #         while curr:
    #             if size > curr.key[0]:
    #                 curr = curr.right
    #             else:
    #                 if not small or curr.key[0] < small.key[0] or (curr.key[0] == small.key[0] and curr.key[1] < small.key[1]):
    #                     small = curr
    #                 curr = curr.left
            
    #         return small

    #     if color == Color.YELLOW:
    #         curr = ro
    #         # Compact fit: largest ID
    #         maxi = None
    #         while curr:
    #             if size > curr.key[0]:
    #                 curr = curr.right
    #             else:
    #                 if not maxi or curr.key[0] < maxi.key[0] or (curr.key[0] == maxi.key[0] and curr.key[1] > maxi.key[1]):
    #                     maxi = curr  
    #                 curr = curr.left  
            
    #         return maxi

    #     if color == Color.GREEN:
    #         #largest capacity (rightmost node)
    #         maxi = ro
    #         while maxi and maxi.right:
    #             maxi = maxi.right
    #         if maxi and size<=maxi.key[0]:

    #             return maxi
    #         else: return None

        
    #     if color == Color.RED:
    #         curr = ro
            
    #         maxi = None

    #         while curr:
    #             if maxi is None or curr.key[0] > maxi.key[0]:  
    #                 maxi = curr
    #             curr = curr.right

            
    #         smallest_id_bin = maxi
    #         curr = maxi
          

           

    #         while curr:
    #             if maxi and smallest_id_bin and  curr.key[0] == maxi.key[0] and curr.key[1] < smallest_id_bin.key[1]:
    #                 smallest_id_bin = curr
    #             curr = curr.left
    #         if maxi and size<=maxi.key[0]:

    #             return smallest_id_bin
    #         else: return None

            
        


    #     return None  # If color doesn't match any case

    
    def suitable_bin(self, size, color):
        ro = self.tree2.root

        if color == Color.BLUE:
            return self._find_smallest_bin(ro, size, None)

        elif color == Color.YELLOW:
            return self._find_largest_id(ro, size, None)

        elif color == Color.GREEN:
            return self._find_largest_capacity(ro, size)

        elif color == Color.RED:
            return self._find_largest_with_smallest_id(ro, size)

        return None  # If color doesn't match any case

    def _find_smallest_bin(self, node, size, small):
        if node is None:
            return small
        if size > node.key[0]:
            return self._find_smallest_bin(node.right, size, small)
        else:
            if small is None or node.key[0] < small.key[0] or (node.key[0] == small.key[0] and node.key[1] < small.key[1]):
                small = node
            return self._find_smallest_bin(node.left, size, small)

    
    def _find_largest_id(self, node, size, maxi):
        if node is None:
            return maxi
        if size > node.key[0]:
            return self._find_largest_id(node.right, size, maxi)
        else:
            if maxi is None or node.key[0] < maxi.key[0] or (node.key[0] == maxi.key[0] and node.key[1] > maxi.key[1]):
                maxi = node
            return self._find_largest_id(node.left, size, maxi)

    def _find_largest_capacity(self, node, size):
        if node is None:
            return None
        largest = self._find_largest_capacity(node.right, size) or node
        if largest and size <= largest.key[0]:
            return largest
        return None

    
    def _find_largest_with_smallest_id(self, node, size):
        maxi = self._find_max(node)
        if maxi and size <= maxi.key[0]:
            smallest_id_bin = self._find_smallest_id(maxi, maxi.key[0], maxi)
            return smallest_id_bin
        return None

    
    def _find_max(self, node):
        if node is None or node.right is None:
            return node
        return self._find_max(node.right)

    
    def _find_smallest_id(self, node, key, smallest_id_bin):
        if node is None:
            return smallest_id_bin
        if node.key[0] == key:
            if smallest_id_bin is None or node.key[1] < smallest_id_bin.key[1]:
                smallest_id_bin = node
        return self._find_smallest_id(node.left, key, smallest_id_bin)



                

    def add_object(self, object_id, size, color):
        target_bin=self.suitable_bin(size,color)
        obj=Object(object_id, size, color)

        
        
        if not target_bin:
            raise NoBinFoundException
        # new_object = Object(object_id, size, color)
    
        self.treeobj.insert(object_id,obj)
        
        # obj.binid=target_bin.key[1]
        
        
        target_bin.value.add_object(obj)
        
        
        id=target_bin.key[1]
        cap=target_bin.key[0]
        val = target_bin.value
        # print('.',self.tree2.inorder(self.tree2.root))
        # self.tree1.remove(id)
        self.tree2.remove(target_bin.key)
        # print('.',self.tree2.inorder(self.tree2.root))
        new_capacity = cap - size
        # target_bin.value.remcapacity=new_capacity
        
        
        # print("kya hua")
        self.tree2.insert((new_capacity,id),val)
        # print("kuch nhi1")
       
        # self.tree1.insert(id,target_bin.value)
        # print(self.tree2.inorder(self.tree2.root))
        
        
        # balance krna hoga ab tree ko like down heap
        # ya us bin ko delete krde or fir add kare after capacity is altered



    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        obj=self.treeobj.search(object_id)
        
        if obj:
           
            ob=obj.value
        else:
            return None
            
           
        # print(self.treeobj.inorder(self.treeobj.root))
        
        self.treeobj.remove(object_id)
        # print(self.treeobj.inorder(self.treeobj.root))
        
        bin_id=ob.binid
        # print(bin_id)
        capi=self.tree1.search(bin_id)
        
        if capi:
            binn=capi.value
            
            binn.remove_object(ob)
            
            # print(binn.objectTree.inorder(binn.objectTree.root))


            capii=binn.remcapacity
            self.tree2.remove((capii-ob.size,bin_id))
            # self.tree1.remove(bin_id)
            self.tree2.insert((capii,bin_id),binn)  #agar dikkat aaye to ek naya variable banake binn assign kar dena
            # self.tree1.insert(bin_id,binn)
        # print(self.tree2.inorder(self.tree2.root))

        

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
            
        # print(self.tree2.inorder(),0)
        # print(self.tree1.inorder(self.tree1.root))
        bin_node = self.tree1.search(bin_id)
       
       
        if bin_node:
            
            return (bin_node.value.remcapacity, bin_node.value.getobj()) 
        return None
        

    def object_info(self, object_id):
       
        obj=self.treeobj.search(object_id)
        if obj:
            
            return obj.value.binid
        else:
            return None
    

    
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None 
        self.right = None
        self.height = 1
    def update_height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = max(left_height, right_height) + 1
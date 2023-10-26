from typing import Self, Optional, List

class AvlTree:
    def __init__(self, key:int, left:Optional[Self]=None, right:Optional[Self]=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self)->str:
        return str(AvlTree.inorder(self, []))
    
    def __repr__(self)->str:
        return str(self)
    
    @staticmethod
    def get_height(root:Optional[Self])->int:
        if not root:
            return 0
        return root.height
    
    def get_height_diff(self)->int:
        left_height = AvlTree.get_height(self.left)
        right_height = AvlTree.get_height(self.right)
        return left_height - right_height

    @staticmethod
    def insert(root:Self, k:int)->Self:
        """
        Insert a key in an AVL BST. Ensures after every insertion operation that the tree is always balanced by performing
        the necessary rebalancing rotations.
        """
        if not root:
            return AvlTree(k)
        if k < root.key:
            root.left = AvlTree.insert(root.left, k)
        elif k > root.key:
            root.right = AvlTree.insert(root.right, k)
        else:
            return root
        
        left_height = AvlTree.get_height(root.left)
        right_height = AvlTree.get_height(root.right)
        root.height = 1 + max(left_height, right_height)
        height_diff = left_height - right_height

        if height_diff > 1: # Meaning we have a left imbalance
            if k < root.left.key: # Meaning we have a left left imbalance
                return root.right_rotate()
            else: # Meaning we have a left right imbalance
                root.left = root.left.left_rotate()
                return root.right_rotate()
        
        if height_diff < -1: # Meaning we have a left imbalance
            if k > root.right.key: # Meaning we have a right right imbalance
                return root.left_rotate()
            else: # Meaning we have a right left imbalance
                root.right = root.right.right_rotate()
                return root.left_rotate()
        
        return root

    @staticmethod
    def delete(root, k:int)->Self:
        if not root:
            return None
        if k < root.key:
            root.left = AvlTree.delete(root.left, k)
        elif k > root.key:
            root.right = AvlTree.delete(root.right, k)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_key = root.right.get_minimum()
                root.key = min_key
                root.right = AvlTree.delete(root.right, min_key)

        left_height = AvlTree.get_height(root.left)
        right_height = AvlTree.get_height(root.right)
        root.height = 1 + max(left_height, right_height)
        height_diff = left_height - right_height

        if height_diff > 1: # Meaning we have a left imbalance
            if root.left.get_height_diff() >= 0: # Meaning we have a left left imbalance
                return root.right_rotate()
            else: # Meaning we have a left right imbalance
                root.left = root.left.left_rotate()
                return root.right_rotate()
        
        if height_diff < -1: # Meaning we have a left imbalance
            if root.right.get_height_diff() <= 0: # Meaning we have a right right imbalance
                return root.left_rotate()
            else: # Meaning we have a right left imbalance
                root.right = root.right.right_rotate()
                return root.left_rotate()
        
        return root
    
    def left_rotate(self)->Self:
        """
        Performs a a simple left rotation.
        """
        right_c = self.right
        right_left_c = right_c.left
        right_c.left = self
        self.right = right_left_c

        #update heights after rotation
        self.height = 1 + max(AvlTree.get_height(self.left), AvlTree.get_height(self.right))
        right_c.height = 1 + max(AvlTree.get_height(right_c.left), AvlTree.get_height(right_c.right))

        return right_c

    def right_rotate(self)->Self:
        """
        Performs a a simple right rotation.
        """
        left_c = self.left
        left_right_c = left_c.right
        left_c.right = self
        self.left = left_right_c
        
        #update heights after rotation
        self.height = 1 + max(AvlTree.get_height(self.left), AvlTree.get_height(self.right))
        left_c.height = 1 + max(AvlTree.get_height(left_c.left), AvlTree.get_height(left_c.right))

        return left_c

    def get_minimum(self)->int:
        """
        Return the minimum key value in the subtree of self.
        """
        if self.left:
            return self.left.get_minimum()
        return self.key
    
    def __contains__(self, k:int)->bool:
        """
        Returns a boolean depending on whether our binary search tree contains the key v.
        """
        current = self
        while current is not None:
            current_k = current.key
            left_child, right_child = current.left, current.right
            if current_k == k:
                return True
            elif k < current_k:
                current = left_child
            else:
                current = right_child
        return False
    
    def __len__(self)->int:
        """
        Returns the number of keys in the AVL tree.
        """
        n_left_subtree = 0
        n_right_subtree = 0
        if self.left is not None:
            n_left_subtree = len(self.left)
        if self.right is not None:
            n_right_subtree = len(self.right)
        return 1 + n_left_subtree + n_right_subtree
    
    @staticmethod
    def inorder(root, r=[])->List[int]:
        """
        Returns an inorder list representation of the binary search tree.
        """
        if root.left:
            r = AvlTree.inorder(root.left, r)
        r.append(root.key)
        if root.right:
            r = AvlTree.inorder(root.right, r)
        return r
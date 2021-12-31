"""Binary search trees"""
# MCS 275 Spring 2021 - David Dumas
# Lecture 20
from binary import Node

class BST:
    """Binary search tree"""
    def __init__(self):
        """Initialize an empty BST with root None"""
        self.root = None

    def insert(self,x):
        """Take a node `x` and insert it into the BST in
        a suitable place"""
        cur = self.root
        prev = None
        while cur != None:
            prev = cur
            if x.key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        if prev == None:
            # This is the first node to be inserted
            self.root = x
        else:
            # Make x a child of prev
            if x.key < prev.key:
                prev.set_left(x)
            else:
                prev.set_right(x)

    def search(self,k):
        """Look for a node with key `k` and return it if
        found, or return None if there is no such node."""
        return self._search(k,self.root)

    def _search(self,k,base):
        """Look for a node with key `k` in the subtree
        with root `base` and return it if found,
        or return None if there is no such node."""
        if base == None:
            return
        # Now we know base is an actual `Node` object
        if k == base.key:
            return base
        # Now we know we know we need to proceed to
        # either the left or right subtree
        if k < base.key:
            return self._search(k,base.left)
        else:
            return self._search(k,base.right)
    
    def minimum(self,x=None):
        """In the subtree with root `x`, find and return a node with
        the smallest key. If `x` is not specified, use `self.root`."""
        if x == None:
            x= self.root

        while x.left != None:
            x = x.left        
        return x
        
    def maximum(self,x=None):
        """In the subtree with root `x`, find and return a node with
        the largest key. If `x` is not specified, use `self.root`."""
        if x == None:
            x= self.root
        while x.right != None:
            x = x.right        
        return x

    def maxDepth (self, x=None):
        sz = 0
        szRight = 0

        if x:
            root = x
        else:
            root = self.root

        if root.left != None:
            sz = 1
            sz += self.maxDepth( root.left)
        if root.right != None:
            szRight = 1
            szRight += self.maxDepth( root.right)
        if sz < szRight:
            sz = szRight

        return sz
    
    def interval(self,x):
        """Given a node `x` with no children, return the minimum and maximum key values
        that could be stored at `x` without violating the BST condition.  The value None
        is used to indicate that the range of allowable values has no upper or lower
        bound."""
        if x == None or x.parent == None:
            return None
        elif x.parent.key < x.key:
            kmin = x.parent
            kmax = self.interval(x.parent)
        elif x.parent.key >= x.key:
            kmin1 = self.interval(x.left)
            kmin2 = self.interval(x.right)
            if kmin1 <= kmin2:
                kmin = kmin1
            else:
                kmin = kmin2 
            kmax = x.parent
        print((kmin, kmax))
        return (kmin, kmax)
        
if __name__ == "__main__":
    
    import treeutil
    import treevis

    T,x = treeutil.random_bst_and_node(nodes=5)
    treevis.treeprint(T)
    print(x, T.interval(x))


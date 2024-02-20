"""
IntervalTreeNode class that represents a node in an interval tree.

Author: Stephen Ruhlen

Version: 1.0
"""
class IntervalTreeNode:

    """
    Constructor method.
    Args:
        val : the value to store in the node
        low : the lower bound of the interval
        high : the upper bound of the interval 
    """
    def __init__(self, val, low, high):
        self.val = val
        self.low = low 
        self.high = high
        self.left = None
        self.right = None
        self.maxEnd = high
    
    """
    Getter method for the upper bound of the node.
    Returns:
        self.high: the upper bound
    """
    def getHigh(self):
        return self.high 
    
    """
    Getter method for the maximum value of the node tree.
    Returns:
        self.maxEnd: the maximum value stored in the tree
    """
    def getMaxEnd(self):
        return self.maxEnd

    """
    Getter method for the lower bound of the node.
    Returns:
        self.low: the lower bound of the interval.
    """
    def getLow(self):
        return self.low

    """
    Getter method for the left child of the node.
    Returns:
        self.left: the left child of the node
    """
    def getLeft(self):
        return self.left 
    
    """
    Getter method for the right child of the node.
    Returns:
        self.right: the right child of the node
    """
    def getRight(self):
        return self.right
    
    """
    Getter method for the node's value.
    Returns:
        self.val: the value stored in the node
    """
    def getValue(self):
        return self.val 
    
    """
    Setter method for the left child of the node.
    Args:
        node: the node to set the left child as
    """
    def setLeft(self, node):
        self.left = node

    """
    Setter method for the right child of the node.
    Args:
        node: the node to set the right child as
    """
    def setRight(self, node):
        self.right = node

    """
    Setter method for the max end of this tree.
    Args:
        num: the max end
    """
    def setMaxEnd(self, num):
        self.maxEnd = num

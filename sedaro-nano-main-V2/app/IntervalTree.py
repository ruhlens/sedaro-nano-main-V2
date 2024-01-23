from IntervalTreeNode import IntervalTreeNode

"""
IntervalTree class.

Author: Stephen Ruhlen

Version: 1.0
"""
class IntervalTree:

    """
    Constructor method.
    """
    def __init__(self):
        self.root = None 
        self.nodeCount = 0

    """
    Method to add a new node to the tree.
    Args:
        low: lower bound of the interval
        high: upper bound of the interval
        val: value to map to the interval
    """
    def add(self, low, high, val):
        self.root = self.__add(self.root, low, high, val)
        self.nodeCount += 1
    
    """
    Recursive helper method for the add method.
    Args:
        node: the current node
        low: the lower bound of the interval
        high: the upper bound of the interval
        val: the value to map to the interval
    Returns:
        node: the current node
    """
    def __add(self, node, low, high, val):
        if node is None:
            return IntervalTreeNode(val, low, high)
        if low < node.getLow():
            node.setLeft(self.__add(node.getLeft(), low, high, val))
        else:
            node.setRight(self.__add(node.getRight(), low, high, val))
        node.setMaxEnd(max(node.getMaxEnd(), high))
        return node

    """
    Method to get list of nodes who's intervals contain a given point.
    Args:
        point: the point to search for
    Returns:
        self.__get(self.root, point, result): the list of nodes who's intervals contain a given point
    """
    def get(self, point):
        result = []
        return self.__get(self.root, point, result)

    """
    Recursive helper method for the get method.
    Args:
        node: the current node
        point: the point to search for
        result: the resulting list
    Returns:
        result: the resulting list
    """
    def __get(self, node, point, result):
        if node is None:
            return result
        if point >= node.getLow() and point <= node.getMaxEnd(): 
            if point < node.getHigh():
                result.append(node.getValue())
            result = self.__get(node.getLeft(), point, result)
            result = self.__get(node.getRight(), point, result)
        return result
    
    """
    Method to return a list containing all of the nodes contained in the tree.
    Returns:
        self.__getTreeList(self.root): The list containing all of the nodes in the tree
    """
    def getTreeList(self):
        return self.__getTreeList(self.root)
    
    """
    Recursive helperm method to the getTreeList method.
    Args:
        node: the current node
    Returns:
        result: the resulting list containing all of the nodes in the tree
    """
    def __getTreeList(self, node):
        if node is None:
            return []
        result = [[node.getLow(), node.getHigh(), node.getValue()]]
        leftTree = self.__getTreeList(node.getLeft())
        rightTree = self.__getTreeList(node.getRight())
        result += leftTree
        result += rightTree
        return result
    
    """
    Getter method for the total node count.
    Returns:
        self.nodeCount: the total number of nodes stored in the trees
    """
    def getNodeCount(self):
        return self.nodeCount

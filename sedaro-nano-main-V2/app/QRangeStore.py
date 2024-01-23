from IntervalTree import IntervalTree

"""
QRangeStore class.
All documentation below holds strong.
Functionally this still works the same, I just changed the mechanics behind it.
"""
class QRangeStore:
    """
    A Q-Range KV Store mapping left-inclusive, right-exclusive ranges [low, high) to values.
    Reading from the store returns the collection of values whose ranges contain the query.
    ```
    0  1  2  3  4  5  6  7  8  9
    [A      )[B)            [E)
    [C   )[D   )
           ^       ^        ^  ^
    ```
    >>> store = QRangeStore()
    >>> store[0, 3] = 'Record A'
    >>> store[3, 4] = 'Record B'
    >>> store[0, 2] = 'Record C'
    >>> store[2, 4] = 'Record D'
    >>> store[8, 9] = 'Record E'
    >>> store[2, 0] = 'Record F'
    Traceback (most recent call last):
    IndexError: Invalid Range.
    >>> store[2.1]
    ['Record A', 'Record D']
    >>> store[8]
    ['Record E']
    >>> store[5]
    Traceback (most recent call last):
    IndexError: Not found.
    >>> store[9]
    Traceback (most recent call last):
    IndexError: Not found.
    """

    """
    Constructor method.
    """
    def __init__(self):
        self.store = IntervalTree()
    
    """
    Method to set using indexing.
    For example, when a user indexes a QRangeStore object as such: QRangeStore[lower,upper] = val it will set that interval (index) to the corresponding val.
    Args:
        rng: the interval to set
        val:  the value to map to the interval
    """
    def __setitem__(self, rng, val):
        (low, high) = rng
        if low >= high:
            raise IndexError("Invalid Range.")
        self.store.add(low, high, val)

    """
    Method to get using indexing.
    For example, when a user indexes a QRangeStore object as such: var = QRangeStore[i] it will access the values at the intervals containing that point.
    Args:
        key: the point to access
    Returns: 
        result: a list containing all values that matched that point
    """
    def __getitem__(self, key):
        result = self.store.get(key)
        if len(result) == 0:
            raise IndexError("Not found.")
        return result
    
    """
    Method to return a list representation of the tree.
    Returns:
        self.store.getTreeList(): a list containing every node in the tree
    """
    def getList(self):
        return self.store.getTreeList()
    
    """
    Method to return the node count.
    Returns:
        self.store.getNodeCount(): the number of nodes in the tree
    """
    def getNodeCount(self):
        return self.store.getNodeCount()
    
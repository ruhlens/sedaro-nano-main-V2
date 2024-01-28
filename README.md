I made the backend code more object oriented and divided it into classes.
I changed the data structure used in the QRangeStore class from a list to an Interval Binary Tree which was just a BST that used the lower bound of the interval of a given node to dictate the node's location in the tree.
I did this to decrease the worst case runtime for the __getitem method from O(n) with the original implementation to O(Log2n) with the BST solution.
I really did not make many changes to the front end aside from a few minor rewrites. 

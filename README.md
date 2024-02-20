I made the backend code more object oriented and divided it into classes.
I changed the data structure used in the QRangeStore class from a list to an Interval Binary Tree which was just a BST that used the lower bound of the interval of a given node to dictate the node's location in the tree.
I did this to decrease the worst case runtime for the __setitem method from O(n) (technically O(1) taking into account amortization, but for the sake of this project I will assume that worst case runtim means that the array size must be doubled and all elements must be copied) with the original implementation to O(Log2n) with the BST solution. It also changes the __getitem method so that, instead of iterating through the list of ranges to values and checking if the given point is within the range of each element, we start at the root node of a BST of ranges to values. We check if the point is within the range of the BST node (lower bound <= point < upper bound), and if it is, we append that value to the returned list and move to the left child node and check the value of the right child node. If point < lower bound, we move to the left child node. If point >= upper bound, we move to the right child node. 
I also made a few changes to clean up the code on the front end and make it more modular.

This implementation of Sedaro Nano shows the versatility of data storage solutions. While the original implementation used a list to store the ranges and corresponding values, this implementation uses what is effectively a binary search tree. The BST does not seem to speed up the program overall, however there is still more to take away from this project. We can see that when we switch the get and add methods (used in QRangeStore's __getItem and __setItem methods) from recursive to while loops, the program speeds up significantly. I believe that this is because using recursive calls overloads the call stack when navigating the BST. 

UPDATES 2/19/2024__
Added Flask API to send data to frontend.__
Restructured File directory to reflect two separate programs: app and backend.__
Rewrote docker files and docker compose to facilitate two separate containers.__


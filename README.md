I made the backend code more object oriented and divided it into classes.
I changed the data structure used in the QRangeStore class from a list to a Interval Binary Tree which was just a BST that used the lower bound of the interval stored in it to dictate the node's location.
I really did not make many changes to the front end aside from a few minor rewrites. 
I am still editing it to make it faster, as the __getitem and __setitem methods are a bit slow right now.
I am currently using recursive calls to navigate the Interval Binary Tree, which I am going to switch to while loops to see if that makes it faster.

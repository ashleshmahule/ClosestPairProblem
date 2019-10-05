# ClosestPairProblem

We are given an array of n points in the plane, and the problem is to find out the closest pair of points in the array. This problem arises in a number of applications. For example, in air-traffic control, you may want to monitor planes that come too close together, since this may indicate a possible collision.

***

# Introduction to K D Tree
K D Tree or K Dimensional Tree is a basically a binary search tree in which the nodes are stored in a K Dimensional point in space.
It is a space partitioning data structure for organisation of points in space.
K D Trees are a special case of binary space partitioning trees.

Every non-leaf node implicitly generates a splitting hyperplane that divides the space into two parts, known as half-spaces.
Points to the left of this hyperplane are represented by left sub-tree of that node and points to the right are represented similarly by the right sub-tree of that node.

The hyperplane direction is chosen in the following way: every node in the tree is associated with one of the k dimensions, with the hyperplane perpendicular to that dimension's axis. So, for example, if for a particular split the "x" axis is chosen, all points in the subtree with a smaller "x" value than the node will appear in the left subtree and all points with larger "x" value will be in the right subtree. In such a case, the hyperplane would be set by the x-value of the point, and its normal would be the unit x-axis.

Here's how a 3D K D tree looks-

![3D K D Tree](https://github.com/ashleshmahule/ClosestPairProblem/blob/master/3dtree.png)

The first split (the red vertical plane) cuts the root cell (white) into two subcells, each of which is then split (by the green horizontal planes) into two subcells. Finally, four cells are split (by the four blue vertical planes) into two subcells. Since there is no more splitting, the final eight are called leaf cells.



***

## Creating a K D Tree
Creation of a K D Tree using python:

Source available here 
    https://github.com/ashleshmahule/ClosestPairProblem/blob/master/creatingKDTree.py

    
    
***

## sklearn.neighbors.KDTree introduction

The function for creating a K D Tree is-

    KDTree(X, leaf_size=40, metric=’minkowski’, **kwargs)

    Parameters:	
    X : array-like, shape = [n_samples, n_features]
           n_samples is the number of points in the data set, and n_features is the dimension of the parameter space. Note: if X is a C-contiguous array of doubles then data will not be copied. Otherwise, an internal copy will be made.

    leaf_size : positive integer (default = 40)
                   Number of points at which to switch to brute-force. Changing leaf_size will not affect the results of a query, but can significantly impact the speed of a query and the memory required to store the constructed tree. The amount of memory needed to store the tree scales as approximately n_samples / leaf_size. For a specified leaf_size, a leaf node is guaranteed to satisfy leaf_size <= n_points <= 2 * leaf_size, except in the case that n_samples < leaf_size.

    metric : string or DistanceMetric object
                The distance metric to use for the tree. Default=’minkowski’ with p=2 (that is, a euclidean metric). See the documentation of the DistanceMetric class for a list of available metrics. kd_tree.valid_metrics gives a list of the metrics which are valid for KDTree.

    Additional keywords are passed to the distance metric class.
    Attributes:	
    data : memory view
            The training data
    
***

### Solution 

Solution File Link 
    https://github.com/ashleshmahule/ClosestPairProblem/blob/master/Assign3.py

Pyximity
========

Pyximity is a Python implementation of the [k-nearest neighbor algorithm](http://en.wikipedia.org/wiki/K-nearest_neighbor_algorithm) for regressing unknown target variables in a two dimensional space.  It's primary use case is solving for unknowns based on a limited set of known points in GIS applications.  However, it can be used for any form of nearest neighbor regression in two dimensions.  Usage requires Python's [numpy](http://numpy.scipy.org/) scientific computing library

The `Pyximity` class has one constructor that takes in two parameters:
* `neighbors`: a numpy array of [x, y] coordinate pairs of the known neighbor points
* `values`: a numpy array of the corresponding values of those neighbor points.

After instantiating `Pyximity`, you can call `regress` on the instance passing in the following:
* `target`: a numpy array of the [x, y] unknown.

As optional parameters:
* `k`: The k of "k-nearest neighbor".  Only the `k` closest neighbors' values will be considered for incorporation into the solution to the target value.  The default value is 5.
* `kernel`: This is the kernel function that determines the weighting of the top `k` neighbors.  The default is the triangular kernel which weakens the weighting of the neighbor value at a linear rate as the distance from the target increases.  If you choose to override this default, the lambda function passed in must take in one parameter: the normalized distance from the target.  That is, a value between 0 and 1 with 1 representing the largest of the `k` distances of the `k` nearest neighbors.  For suggestions on functions to use as kernels, consider using [Kernel Density Functions](http://en.wikipedia.org/wiki/Kernel_%28statistics%29) as criteria. If you wish to have a simple arithmetic mean of the `k` neighbors, you may pass a lambda that simply returns 1.

The method returns the regressed value of the unknown coordinate based on the average of the k nearest neighbors calculated according to the kernel function.
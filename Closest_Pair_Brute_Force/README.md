## LAB 4 – Closest Pair (Brute Force)
GECHLENG LIM <br>
COMP2350: ALGORITHMS

This program implements the brute-force closest pair algorithm, which finds the two closest points in a set of two-dimensional points by comparing every unique pair. The algorithm computes the squared Euclidean distance between each pair and keeps track of the minimum distance found, resulting in a time complexity of Θ(n²).

One challenge I faced was understanding what each loop was iterating over. At first, I thought the inner loop should iterate over the x and y coordinates inside a point, which led to incorrect indexing. I later realized that both loops iterate over the list of points, with the outer loop selecting a reference point and the inner loop comparing it to the remaining points. I also struggled with correctly accessing coordinates and initially confused expressions like points[i][0] with incorrect forms such as points[0][i]. Tracing the code step by step helped clarify that the first index selects the point and the second index selects the coordinate.

Another difficulty was handling variable scope inside the function. I initially tried to update variables defined outside the function, which resulted in incorrect output values. Refactoring the function to define variables locally and return the closest pair and distance resolved this issue. Through this lab, I gained a clearer understanding of brute-force algorithm structure, indexing, and Python function behavior.

## Sample Output
### Brute-Force Closest Pair Output:

Input:<br>
Points: [[1, 4], [2, 8], [5, 5], [6, 7], [3, 2], [9, 1], [4, 3]]<br>
Output:<br>
Closest coordinate: [3, 2] and [4, 3]<br>
Squared distance: 2
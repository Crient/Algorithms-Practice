## LAB 5 – Convex Hull (Brute Force)

GECHLENG LIM <br>
COMP2350: ALGORITHMS

This program implements the brute force convex hull algorithm, which identifies the boundary edges of the smallest convex polygon that encloses a given set of two dimensional points. The algorithm works by examining every unique pair of points as a potential edge and checking whether all remaining points lie on the same side of the line formed by that pair. If no points appear on both sides of the line, the segment is considered part of the convex hull boundary. Because the algorithm checks all point pairs and compares them against all other points, it runs in Θ(n³) time.

The core challenge of this lab was translating the geometric definition of a convex hull into precise code logic. Initially, I understood the high level idea but struggled with how to correctly implement it using nested loops and indexing. One major issue was confusing point indexes with coordinate indexes. At first, I treated variables like i and j as if they selected x and y values, leading to incorrect expressions such as points[i][i]. Through debugging, I learned that the first index always selects a point from the list, while the second index selects a coordinate within that point.

Another difficulty was understanding how to correctly check “all other points” for a given edge. I initially tried starting the inner loop at a fixed index, thinking this represented checking n minus two points. I later realized that this approach skips specific points in the list rather than dynamically excluding the two endpoints of the candidate edge. The correct approach was to loop through the entire list of points and explicitly skip the indexes corresponding to the two endpoints. This distinction clarified the difference between the number of points being checked and which points must be checked for correctness.

I also struggled with interpreting the sign checking logic used to determine whether points lie on one side of a line. Implementing counters for positive and negative values helped me understand how sign consistency directly maps to the convex hull condition. Adding an additional condition to ensure at least one point lies strictly on one side of the line prevented degenerate and interior edges from being incorrectly included in the result.

By the end of this lab, I gained a much stronger understanding of how brute force geometric algorithms are structured, how theoretical conditions translate into concrete checks, and how small indexing or loop mistakes can lead to incorrect results even when the overall idea is correct. This lab also reinforced careful debugging and step by step reasoning as essential skills when working with nested loops and geometry based algorithms.

##  Sample Output
### Brute Force Convex Hull Output:

Input:<br>
Points:
[(1, 1), (1, 4), (4, 4), (4, 1), (2, 2), (3, 2), (2, 3)]<br>

Output:<br>
Convex Hull Boundary Edges:<br>
((1, 1), (4, 1))<br>
((4, 1), (4, 4))<br>
((4, 4), (1, 4))<br>
((1, 4), (1, 1))
## LAB 7 – Quickselect

GECHLENG LIM <br>
COMP2350: ALGORITHMS

This program implements the Quickselect algorithm, which finds the k-th smallest element in an unsorted array without fully sorting the list. The algorithm works by choosing a pivot, partitioning the array so that smaller elements move to the left and larger elements move to the right, and then checking the pivot’s final position. If the pivot lands at index k minus 1, the answer has been found. If it lands too far to the right, the algorithm continues on the left subarray. If it lands too far to the left, it continues on the right subarray. Because Quickselect only recurses into one side of the partition, its average running time is Θ(n), while its worst case running time is Θ(n²).

The main challenge of this lab was understanding how partitioning supports the overall Quickselect logic. At first, I understood the goal of finding the k-th smallest element, but I was confused about how the pivot’s final index determines which side of the array should be searched next. I had to separate the meaning of k, which is the rank of the element I want, from the pivot index after partitioning. Once I understood that the pivot’s final position tells me how many elements are smaller than it, the recursive step became much clearer.

Another difficulty was translating the pseudocode into Python while keeping track of the left and right boundaries of the current subarray. I initially mixed up full array indexing with subarray logic, which caused confusion about how recursive calls should update the boundaries and whether the pivot should still be included. I later understood that once the pivot is in its final position, the recursion continues only on the side that could still contain the answer.

By the end of this lab, I gained a stronger understanding of partition based selection, recursive problem reduction, and the importance of careful indexing and boundary control for correctness.

## Sample Output
### Quickselect Output:

Input:<br>
Array: [4, 1, 10, 8, 7, 12, 9, 2, 15]<br>
k = 5<br>

Output:<br>
The 5th smallest element is: 8
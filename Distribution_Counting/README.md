# LAB 8 – Distribution Counting Algorithm

GECHLENG LIM <br>
COMP2350: ALGORITHMS

This program implements the distribution counting algorithm, which is a non-comparison based sorting method that works efficiently when the input values come from a limited range. Instead of comparing elements like traditional sorting algorithms, this approach counts how many times each value appears and then uses that information to determine the correct position of each element in the sorted array.

The algorithm uses an auxiliary array D to store frequency counts of each value in the input array. Each value in the original array is mapped to an index in D using the expression (A[i] - l), where l is the minimum value in the range. After counting frequencies, the algorithm updates D to store cumulative distribution values. These values represent how many elements are less than or equal to a given value, which allows the algorithm to compute exact positions in the output array.

In the final step, the algorithm builds the sorted array S by iterating through the input array in reverse order. For each element, it uses the distribution values in D to place the element into its correct position in S, and then updates D accordingly. The reverse traversal ensures that the algorithm remains stable, meaning that duplicate values maintain their original relative order.

Because the algorithm avoids comparisons and instead relies on counting and indexing, it runs in linear time when the range of values is fixed. This makes it more efficient than comparison-based sorting algorithms in specific cases, although it requires additional space for the counting array.

One challenge in this lab was correctly translating the pseudocode into working code, especially handling the index mapping with (A[i] - l) and adjusting loop boundaries to match Python’s range behavior. Another difficulty was understanding how the array D changes its role throughout the algorithm, from storing frequencies to storing distribution values. Once that transition became clear, the overall logic of the algorithm was much easier to follow.

This lab helped reinforce the concept of space-for-time tradeoffs, where extra memory is used to improve time efficiency, and showed how preprocessing input data can eliminate the need for comparisons in sorting.

## Sample Output

### Input:
A = [13, 11, 12, 13, 12, 12], l = 11, u = 13

Frequency Array D:<br>
[1, 3, 2]

Distribution Array D:<br>
[1, 4, 6]

Sorted Output S:<br>
[11, 12, 12, 12, 13, 13]
## LAB 2 – Bubble Sort and Sequential Search
GECHLENG LIM <br>
COMP2350: ALGORITHMS

This program implements two brute-force algorithms: Bubble Sort and Sequential Search. I began by working on the Bubble Sort portion, which was easier for me to understand because the steps are very visual and repetitive. By comparing adjacent elements and swapping them when they were out of order, I could clearly see how larger values gradually moved to the end of the list after each pass. Printing the array after each swap helped me confirm that the algorithm was behaving correctly.

I spent much more time working on the Sequential Search portion of the lab. I struggled with loop control, return placement, and understanding when the algorithm should stop searching. I often returned values too early and did not allow the loop to check every element in the list. After carefully tracing the code step by step and testing different input cases, I was able to correct the control flow so the search only returns an index when the key is found and returns −1 only after the entire list has been checked. This process helped me better understand how small logic mistakes can significantly affect algorithm correctness.

## Sample Output

Initial List: Array = [80, 23, 45, 12, 67, 34, 89, 10]

#### Bubble Sort Output (intermediate steps shown):  
[23, 80, 45, 12, 67, 34, 89, 10]  
[23, 45, 80, 12, 67, 34, 89, 10]  
[23, 45, 12, 80, 67, 34, 89, 10]  
...  
[10, 12, 23, 34, 45, 67, 80, 89]

#### Sequential Search Output (intermediate steps shown):  
- Input:<br>
What number do you want to search for: 89<br>
Output: 7

- Input:<br>
What number do you want to search for: 90<br>
Output: -1

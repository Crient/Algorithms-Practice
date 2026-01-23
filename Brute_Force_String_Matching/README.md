## LAB 3 – Brute-Force String Matching
GECHLENG LIM <br>
COMP2350: ALGORITHMS

This program implements the brute-force string matching algorithm, which searches for a smaller pattern inside a larger text by checking every valid starting position and comparing characters one by one. One of the main difficulties I encountered was determining the correct boundary for the outer loop, specifically the line `for i in range(0, len(T) - len(P) + 1)`. I initially misunderstood how Python’s `range` function works and made several off-by-one errors, which caused the algorithm to miss valid matches at the end of the text or attempt to access characters outside the text.

I also struggled with understanding the logic inside the inner loop, especially the condition `while j < len(P) and P[j] == T[i + j]` and the success check `if j == len(P)`. At first, I thought the algorithm needed some kind of key or additional data structure, such as a hash map, to confirm that the entire pattern had been matched. I did not realize that the algorithm relies purely on counting how many characters match consecutively. After tracing the code step by step, I learned that incrementing `j` only when characters match allows the algorithm to confirm a full match once `j` reaches the length of the pattern. This helped me understand that no characters are overwritten and no extra storage is required, and that careful loop control is the core of the brute-force approach.

## Sample Output
#### Brute-Force String Matching Output:

- Input:<br>
Input your text: HELLO<br>
What do you want to find: LL<br>
Output: 2

- Input:<br>
Input your text: COMPUTER<br>
What do you want to find: PUT<br>
Output: 3

- Input:<br>
Input your text: ABCDE<br>
What do you want to find: FG<br>
Output: -1

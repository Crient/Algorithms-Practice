# GECHLENG LIM
# COMP2350 - ALGORITHMS
# LAB 1 - Sieve of Eratosthenes
This program uses the Sieve of Eratosthenes algorithm to find all prime numbers less than or equal to a user input value n. The program first creates a list of consecutive integers starting from 2 up to n, which represents all possible prime candidates. It then loops through the list while the current number is less than or equal to the square root of n, since any multiples beyond that point would have already been removed. For each valid number, the program eliminates its multiples by setting them to zero in the list. Because the list starts at the value 2, there is a difference between the actual number values and their list indices, which is handled using nums[j - 2] = 0 to correctly mark eliminated numbers. After the sieving process is complete, all remaining non zero values are collected as prime numbers. The program prints the original list, the crossed out list, and the final list of primes to clearly show how the algorithm works step by step.

* Sample Output
Input: n = 5
======================= 
Output:
 - Your number:  5 
 - Original Numbers: [2, 3, 4, 5] 
 - Number Crossing: [2, 3, 0, 5] 
 - ResultPrime Numbers: [2, 3, 5]

Input: n = 50
======================= 
Output:
 - Your number:  50 
 - Original Numbers: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50] 
 - Number Crossing: [2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0, 0, 0, 23, 0, 0, 0, 0, 0, 29, 0, 31, 0, 0, 0, 0, 0, 37, 0, 0, 0, 41, 0, 43, 0, 0, 0, 47, 0, 0, 0] 
 - ResultPrime Numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
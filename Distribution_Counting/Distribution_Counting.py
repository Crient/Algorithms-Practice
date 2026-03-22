A1 = [4, 2, 7, 1]
l1 = 1
u1 = 7

A2 = [5, 3, 5, 2, 3, 2]
l2 = 2
u2 = 5

A3 = [13, 11, 12, 13, 12, 12]
l3 = 11
u3 = 13

def distribution_counting_sort(A, l, u):
    n = len(A)

    # create counting array D
    D = [0] * (u - l + 1)

    # create output array S
    S = [0] * n

    # Loop 1: initialize frequencies
    for j in range(0, u - l + 1):
        D[j] = 0
    
    # Loop 2: compute frequencies
    for i in range(0, n):
        D[A[i] - l] = D[A[i] - l] + 1

    # Loop 3: convert to distribution values
    for j in range(1, u - l + 1):
        D[j] = D[j - 1] + D[j]
    
    # Loop 4: place elements into sorted array
    for i in range(n - 1, -1, -1):
        j = A[i] - l
        S[D[j] - 1] = A[i]
        D[j] = D[j] - 1
  
    return S

print("Test Case 1: Distinct Values")
print("Input:", A1)
print("Sorted:", distribution_counting_sort(A1, l1, u1))

print("Test Case 2: Repeated Values")
print("Input:", A2)
print("Sorted:", distribution_counting_sort(A2, l2, u2))

print("Test Case 3: Minimum Value is Not 0")
print("Input:", A3)
print("Sorted:", distribution_counting_sort(A3, l3, u3))

# ===============================
# LAB 8 – SHORT ANSWERS
# ===============================

# 1. What is the purpose of array D?
# Array D is used to keep track of the values in the input array. At first, it counts how many times each number appears.
# After that, it gets updated to store cumulative values, which tell how many elements are less than or equal to each value.
# This helps the algorithm figure out the correct position of each number in the sorted array.

# 2. Why does the algorithm first count frequencies and then convert them into distribution values?
# The algorithm first counts frequencies so it knows how many times each value shows up.
# Then it converts those into distribution values so it can determine where each value should go in the final sorted array.
# Just knowing the counts is not enough, because you also need positions, and that is what the distribution step gives.

# 3. Why does the last loop go from n - 1 downto 0?
# The loop goes backward to make sure the sorting stays stable.
# That means duplicate values keep their original order.
# If we loop forward, that order could get messed up.

# 4. Under what condition is this algorithm efficient?
# This algorithm works best when the values are integers and the range between the minimum and maximum is small.
# If the range is too large, the extra array D becomes too big and it is not efficient.

# 5. What is the time complexity when the range of values is fixed?
# The time complexity is O(n) because the algorithm makes a few linear passes through the data.
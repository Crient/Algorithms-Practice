A = [4, 1, 10, 8, 7, 12, 9, 2, 15]
print("Find your number:", A)

k = int(input("What kth number do you want to find: "))

def partition(A, left, right):
    l = left
    r = right
    p = A[l]
    s = l

    for i in range(l + 1, r + 1):
        if A[i] < p:
            s = s + 1
            A[s], A[i] = A[i], A[s]

    A[l], A[s] = A[s], A[l]
    return s

def quick_select(A, left, right, k):
    s = partition(A, left, right)

    if s == k - 1:
        return A[s]
    elif s > k - 1:
        return quick_select(A, left, s - 1, k)
    else:
        return quick_select(A, s + 1, right, k)

if k >= 1 and k <= len(A):
    result = quick_select(A, 0, len(A) - 1, k)
    print(f"The {k}th smallest element is: {result}")
else:
    print("Invalid k")
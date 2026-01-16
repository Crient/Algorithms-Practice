# Initial list
Array = [80, 23, 45, 12, 67, 34, 89, 10]

# Bubble Sort
for i in range(0, len(Array) - 1):
    for j in range(0, len(Array) - 1 - i):
        if Array[j + 1] < Array[j]:
            Array[j], Array[j + 1] = Array[j + 1], Array[j]
            print(Array)

# User input for search key
K = int(input("What number do you want to search for: "))

# Sequential Search
def sequential(Array):
    for i in range(0, len(Array)):
        if Array[i] == K:
            return i
    return -1

print(sequential(Array))

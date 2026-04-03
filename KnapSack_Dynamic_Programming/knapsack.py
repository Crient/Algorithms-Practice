def knapsackDP(weights, values, n, W):
    # 1. Create table F[0..n][0..W]
    F = [[0 for j in range(W + 1)] for i in range(n + 1)]

    # 2. For j = 0 to W, set F[0][j] = 0
    for j in range(W + 1):
        F[0][j] = 0

    # 3. For i = 0 to n, set F[i][0] = 0
    for i in range(n + 1):
        F[i][0] = 0

    # 4. For i = 1 to n
    for i in range(1, n + 1):
        # For j = 1 to W
        for j in range(1, W + 1):
            # If weights[i] > j
            if weights[i - 1] > j:
                # F[i][j] = F[i - 1][j]
                F[i][j] = F[i - 1][j]
            else:
                # F[i][j] = max(F[i - 1][j], values[i] + F[i - 1][j - weights[i]])
                F[i][j] = max(F[i - 1][j], values[i - 1] + F[i - 1][j - weights[i - 1]])

    # 5. maxValue = F[n][W]
    maxValue = F[n][W]

    # 6. Set j = W
    j = W
    selected_items = []

    # 7. For i = n down to 1
    for i in range(n, 0, -1):
        # If F[i][j] != F[i - 1][j]
        if F[i][j] != F[i - 1][j]:
            # item i is included
            selected_items.append(i)
            j = j - weights[i - 1]
        # Else item i is not included

    selected_items.reverse()

    # 8. Print the DP table
    print("DP Table:")
    for row in F:
        print(row)

    # 9. Print maxValue
    print("Maximum value =", maxValue)

    # 10. Print selected items
    print("Selected items =", selected_items)

  
weights = [2, 3, 4, 5]
values = [1, 2, 5, 6]
n = 4
W = 8

knapsackDP(weights, values, n, W)
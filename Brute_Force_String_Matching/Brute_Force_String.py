T = input("Input your text: ")        # The main text where we search
P = input("What do you want to find: ")  # The pattern we are looking for

def string_find(T, P):
    # Loop through every valid starting index in T
    # The pattern must fully fit starting at i
    for i in range(0, len(T) - len(P) + 1):

        j = 0  # Counts how many characters of P have matched so far

        # While we are still inside the pattern AND
        # the current pattern character matches the aligned text character:
        # - j tracks how many characters of P have matched so far
        # - i is the starting index in T
        # - i + j aligns the j-th character of P with the correct character in T
        # If the first character mismatches, this loop never runs and we move to i+1
        while j < len(P) and P[j] == T[i + j]:
            j = j + 1  # Move to the next character in P

            # If j reached the length of P,
            # it means all characters matched
            if j == len(P):
                return i  # Return the starting index of the match

    # If no match was found after checking all positions
    return -1

print(string_find(T, P))  
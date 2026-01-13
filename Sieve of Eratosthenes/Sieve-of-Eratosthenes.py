import math

n = int(input("Give us a number: "))
nums = []
result = []

# Create a list of numbers from 2 to n
for i in range(2, n + 1):
    nums.append(i)

# Creating Floor Function
original_nums = nums.copy()
n_floor = math.floor(math.sqrt(n))

#Looping between nums to get rid of multiplication
for i in range(n_floor):
    if nums[i] != 0:
        j = nums[i] * nums[i]
        while j <= n:
            nums[j - 2] = 0
            j = j + nums[i]
           
#Assigning and printing result
for i in range(len(nums)):
    if nums[i] != 0:
        result.append(nums[i])

print("=======================", "\n"
      " - Your number: ", n, "\n"
      " - Original Numbers:", original_nums, "\n"
      " - Number Crossing:", nums, "\n"
      " - Result Prime Numbers:", result)  


    


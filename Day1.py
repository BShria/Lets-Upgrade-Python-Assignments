# Assignment: Take multiple numbers through input and print the sum of the numbers.

nums = [int(i) for i in input('Enter numbers: ').split()]
sum = 0
for i in nums:
  sum += i
print(sum)

# Input: 
# Enter numbers: 10 40 20 50
# Output: 120
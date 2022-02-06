# Use filter function to filter out the elements from a list that are divisible by 3 & 5

li = [int(i) for i in input('Enter numbers: ').split()]
print(list(filter(lambda n: ((n%3 == 0 ) & (n%5 == 0)), li)))
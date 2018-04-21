# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

multiples_3 = [list(x / 3) for x in range(100) if x % 3 == 0]# write your list comprehension here
print(multiples_3)
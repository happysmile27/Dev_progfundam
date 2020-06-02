x = (1, 2, 4, 5, 7, 6, 6, 2, 3, 6, 9, 10, 1)
even = 0
odd = 0
for num in x:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even: " + str(even))
print("Odd: " + str(odd))

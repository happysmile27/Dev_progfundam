my_list = [12,24,35,70,88,120,155]
my_list = [x for (i, x) in enumerate(my_list) if i not in (0, 4, 5)]
print(my_list)
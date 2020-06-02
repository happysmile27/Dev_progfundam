list_one = [3, 6, 9, 12, 15, 18, 21]
list_two = [4, 8, 12, 16, 20, 24, 28]

for i in list_one:
    odd_index = list_one[1::2]

for j in list_two:
    even_index = list_two[0::2]

new_list = odd_index + even_index
print(list(new_list))


my_dict1 = {'a': 100, 'b': 200, 'c':300}
my_dict2 = {'a': 300, 'b': 200, 'd':400}

new_dict = dict(my_dict2)
new_dict.update(my_dict1)
for a, b in my_dict2.items():
    for c, d in my_dict1.items():
        if a == c:
            new_dict[a] = (b + d)
print(new_dict)



# for key in my_dict2:
#     if key in my_dict1:
#         my_dict2[key] = my_dict2[key] + my_dict1[key]
#     else:
#         pass
#
# print(my_dict2)



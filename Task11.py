my_dict = {'a': 100, 'b': 50, 'c': 200, 'd': 1000, 'e': 1, 'f': 300}

new = sorted(my_dict, key=my_dict.get, reverse=True)
print(new[:3])
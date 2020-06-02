my_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
numb = {}
for x in my_list:
    if x in numb:
        numb[x] += 1
    else:
        numb[x] = 1
for key, value in numb.items():
    print(f"{key} : {value}")

my_string = "P@#yn26at^&i5ve"

word_characters = 0
digits = 0
symbols = 0
for i in my_string:
    if i.isalpha():
        word_characters +=1
    elif i.isdigit():
        digits += 1
    else:
        symbols += 1


print("Word characters: " + str(word_characters))
print("Digits: " + str(digits))
print("Symbols: " + str(symbols))







# word_characters = sum(i.isalpha() for i in my_string)
# digits = sum(i.isdigit() for i in my_string)
# symbols =
# print(word_characters)
f = 0

for f in range(0, 10):
    if f not in (2, 5, 8):
        f += 1
        print(f"I have reached the {f} floor")

else:
    print("Harray!")

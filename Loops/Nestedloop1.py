print("Loop Type 1")
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end="")
    print()

print("Loop Type 2")
for i in range(1, 6):
    for j in range(i, 6):
        print("*", end="")
    print()

print("Loop Type 3")
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()

print("Loop Type 4")
for i in range(1, 6):
    for j in range(1, 6):
        print(i, end="")
    print()
print("Loop Type 5")
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end="")
    print()
print("Loop Type 6")
for i in range(1, 6):
    n = i
    for j in range(1, 6):
        print(n, end="")
        n = n+1
    print()

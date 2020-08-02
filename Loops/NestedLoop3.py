print("Loop Type 7")
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end="")
    print()
print("Loop Type 8")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
print("Loop Type 9")
for i in range(1, 6):
    n = i
    for j in range(1, i+1):
        print(n, end="")
        n = n+1
    print()

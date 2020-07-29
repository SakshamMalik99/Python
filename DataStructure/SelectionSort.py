x = [7, 89, 54, 5, 6, 12, 32, 54, 78, 13, 46, 79, 123, 65]
for i in range(0, 12):
    pos = i
    low = x[pos]
    for j in range(i+1, 13):
        if(low > x[j]):
            pos = j
            low = x[j]
    x[i], x[pos] = x[pos], x[i]

print("Sorted Array :")
for i in x:
    print(i, end=" ")

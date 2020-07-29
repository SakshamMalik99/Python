x = [21, 5, 64, 79, 86, 58, 25, 51, 62, 32, 13, 159, 98, 8, 45]
for i in range(1, 13):
    j = i-1
    temp = x[i]
    while(temp < x[j] and j >= 0):
        x[j+1] = x[j]
        j = j-1
    x[j+1] = temp

print("Sorted Array :")
for i in x:
    print(i, end=" ")

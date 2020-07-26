M = input()
m = input().split()
N = input()
n = input().split()

print(*sorted(list(set(m) ^ set(n)), key=int), sep="\n")

n = int(input())
a = list()
b = list()
for i in range(n):
    c = input().split()
    a.append(c)
lst = set()
for i in range(n):
    for j in range(len(a[i])):
        lst.add(a[i][j])
t = 0
for i in lst:
    t += 1
print(t)
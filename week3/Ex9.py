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
A = dict()
for i in lst:
    A[i] = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] in A:
            A[a[i][j]]+=1
m = A[a[i][j]]
n = a[i][j]
for i in lst:
    if A[i]>m:
        m = A[i]
        n = i
    if A[i] == m and i < n:
        m = A[i]
        n = i
print(n)

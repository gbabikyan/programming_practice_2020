n = int(input())
A = dict()
for i in range(n):
    c = input().split()
    A[c[0]] = c[1]
c = input()
if c in A.values():
    for key in A:
        if A[key] == c:
            print(key)
else:
    print(A[c])

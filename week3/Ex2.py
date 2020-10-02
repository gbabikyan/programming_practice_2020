a = list(map(int,input().split()))
max1 = -2147483647
min1 = 2147483647
maxi = 0
mini = 0
for i in range(len(a)):
    if a[i] > max1:
        max1 = a[i]
        maxi = i
    if a[i] < min1:
        min1 = a[i]
        mini = i
a[mini] = max1
a[maxi] = min1
for i in range(len(a)):
    print(a[i])
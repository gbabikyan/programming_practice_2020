a = list(map(int,input().split()))
max = 0
for i in range(len(a)-1):
    if i == 0:
        continue
    if (a[i]>a[i-1]) and (a[i]>a[i+1]):
        max+=1
print(max)

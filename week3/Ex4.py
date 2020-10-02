a = list(map(int,input().split()))
b = list()
for i in range(len(a)):
    t=0
    for j in range((len(a))):
        if a[i] == a[j]:
            t+=1
    b.append(t)
for i in range(len(a)):
    if b[i] == 1:
        print(a[i])

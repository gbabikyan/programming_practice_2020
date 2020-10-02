a = list(map(int,input().split()))
b = list((map(int,input().split())))
c = list()
for i in range(len(a)):
    t=0
    for j in range((len(b))):
        if a[i] == b[j]:
            t+=1
    if t != 0:
        c.append(a[i])

for j in range(len(c)):
    for i in range(len(c) - 1):
        if c[i]>c[i+1]:
            m = c[i+1]
            c[i+1] = c[i]
            c[i] = m
for i in range(len(c)):
    if i == 0:
        print(c[i])
    elif c[i] == c[i-1]:
        continue
    else:
        print(c[i])

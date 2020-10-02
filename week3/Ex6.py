a = list(map(int,input().split()))

for i in range(len(a)):
    t=0
    for j in range(i):
        if a[i] == a[j]:
            print("YES")
            t =1
            break
    if t==0:
        print("NO")

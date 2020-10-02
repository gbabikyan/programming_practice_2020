a = list(map(int,input().split()))
t = 0
for i in range(len(a)):
    for j in range((len(a))):
        if a[i] == a[j] and i != j:
            t += 1
t = t / 2
print(t)

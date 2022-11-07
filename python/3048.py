n = int(input())
a,s = 0,0
for i in range(n):
    v = int(input())
    if v != a:
        a = v
        s += 1
print(s)

p = int(input())
if 1<=p<=5:
    sum = 0
    for i in range(p):
        a,q = input().split()
        if 1<=int(q)<=500:
            sum += (int(a[3])+0.5)*int(q)
    print("%.2f"%sum)

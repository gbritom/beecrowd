MAX = 2**32-1
while True:
    x,m = input().split()
    x = int(x)
    m = int(m)
    if (x == 0 and m == 0):
        break
    elif 0<x<=3 and 10<=m<=MAX:
        print(x*m)

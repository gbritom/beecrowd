def log_seq(n):
    for i in range(1, n+1):
        a = i**2
        b = i**3
        print(i, a, b)
        print(i, a+1, b+1)
var = int(input())
if 1<var<1000:
    log_seq(var)

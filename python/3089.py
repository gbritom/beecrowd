#wip
MAX_V = 10**8
pair = []
n = []
while n != 0:
    n = input().split() # >1 2 = '1','2'
    n = int(n[0])       # becomes 1, 2
    if  n == '':
        break
    elif 2 <= 2*n <= 10**4: 
        x = input().split() 
        x = list(map(int, x)) 
        h, h1, h2 = [0]*3
        l, l1, l2 = [MAX_V]*3
        if 1 <= x[0] <= MAX_V:
            for i in range(2*n):
                sum1 = x[i] + x[2*n-i-1]
                if h <= sum1:
                    h, h1, h2 = sum1, x[i], x[2*n-i-1]
                if l >= sum1:
                    l, l1, l2 = sum1, x[i], x[2*n-i-1]
            pair.append(h)
            pair.append(l)
for i in range(len(pair)//2):
    a,b = max(pair[i*2], pair[i*2+1]), min(pair[i*2], pair[i*2+1])
    print(a,b)

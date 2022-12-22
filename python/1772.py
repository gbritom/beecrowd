def swap(c, i, j):
    c = list(c)[::-1]
    c[i], c[j] = c[j], c[i]
    return ''.join(c)[::-1]
output = []
while True:
    n, k = map(int,input().split())
    num = '{0:032b}'.format(n)
    ma, mi = n, n
    if n == 0 and k == 0:
        break
    else:
        while k>0:
            a,b = map(int, input().split())
            if a == 0 and b == 0:
                 break
            num = swap(num,a,b)
            if mi>int(num,2):
                mi = int(num,2)
            if ma<int(num,2):
                ma = int(num,2)
            k-=1
        output.append(int(num,2))
        output.append(ma)
        output.append(mi)
        
for i in range(0,len(output),3):
    print(output[i],output[i+1],output[i+2])

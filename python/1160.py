n_teste = int(input())
for teste in range (0, n_teste):
    val = input().split()
    pa = int(val[0])
    pb = int(val[1])
    g1=float(val[2])/100
    g2=float(val[3])/100
    n = 0 
    while True:
        pa+=int(pa*g1)
        pb+=int(pb*g2)
        n+=1 
        if pa>pb or n>100:
            break
    if n<=100:
        print(n,'anos.')
    else:
        print("Mais de 1 seculo.")    

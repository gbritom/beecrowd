def nota_esquecida(a,m):
    return m*2-a
    
a = int(input())
m = int(input())
if 0<=a<=100 and 0<=m<=100:
    print(nota_esquecida(a,m))

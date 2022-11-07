import math
def xadrez(n):
    if n >=2 or n<=1000:
        a = math.ceil(n**2/2)
        if n%2==0:
            return a,a
        else:
            return a,a-1
            
c = xadrez(int(input()))
print(f"{c[0]} casas brancas e {c[1]} casas pretas")

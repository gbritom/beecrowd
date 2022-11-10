import math
def primeCheck(x):
    sta = 1
    for i in range(2,int(math.sqrt(x))+1): # range[2,sqrt(num)]
        if(x%i==0):
            sta=0
            return False
        else:
            continue
    if (sta==1):
        return True
        
n = int(input())
while True:
    if primeCheck(n) and primeCheck(n-2):
        print(n-2,n)
        break
    else:
        n-=1

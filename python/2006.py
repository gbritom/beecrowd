t = int(input())
chas = list(input().split())
chas = map(int,chas)
quant = 0
for i in chas:
    if t == i:
        quant+=1
print(quant)

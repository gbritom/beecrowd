import math
x1,y1 = list(map(float,input().split()))
x2,y2 = list(map(float,input().split()))
dist = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
print(f"{dist:.4f}")
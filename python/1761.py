import math
pi = 3.141592654
while True:
    try:
        a,b,c = map(float, input().split())
        print(f"{round((math.tan(a*pi/180)*b+c)*5,2):.2f}")
    except:
        break

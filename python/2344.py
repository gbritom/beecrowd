n = int(input())
if 0<=n<=100:
    if n>0 and n<=35:print("D")
    elif n>35 and n<=60:print("C")
    elif n>60 and n<=85:print("B")
    elif n>85 and n<=100:print("A")
    else:print("E")

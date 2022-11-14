s = int(input())
m = (s//60)%60
h = s//(3600)
s = s%60
print(f"{h:.0f}:{m:.0f}:{s}")
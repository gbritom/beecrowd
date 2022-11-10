a = int(input())
y = a // 365
m = (a - y *365) // 30
d = (a - y * 365 - m*30)
print(f"{y} ano(s)\n{m} mes(es)\n{d} dia(s)")

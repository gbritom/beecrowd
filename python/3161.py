n, m = input().split()
n, m = int(n), int(m)
text = ''
fruit = []
count = 0

for i in range(n):
    fruit.append(input().lower())
    
    
for i in range(m):
    text += input().lower()

for i in range(n):
    if fruit[i] in text or fruit[i][::-1] in text:
        print(f"Sheldon come a fruta {fruit[i]}")
    else:
        print(f"Sheldon detesta a fruta {fruit[i]}")

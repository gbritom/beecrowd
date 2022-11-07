n = int(input())
sum = 0
for i in range(n):
    a = input().split()
    sum+=int(a[0])*int(a[1])
print(sum)

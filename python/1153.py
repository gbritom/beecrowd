def fat(n):
    if n==1:
        return n
    else:
        return n*fat(n-1)
n = int(input())
print(fat(n))

n , s = input().split()
n = int(n)
s = int(s)
lowest, sum = s,s
if 1 <= n <= 30:
    if -10**3 <= s <= 10**3:
        for i in range(n):
            a = int(input())
            sum += a
            if sum < lowest:
                lowest = sum
print(lowest)

entry = input().split()
for i in range(len(entry)):
    entry[i]=int(entry[i])
for i in range(entry[1]):
    if input()=='fechou':
        entry[0]+=1
    else:
        entry[0]-=1
print(entry[0])

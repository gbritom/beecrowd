x = input().split()
x = list(map(int, x))
if (x[0]+x[1]+x[2]+x[5] >= x[3]+x[4]):
    print("Middle-earth is safe.")
else: 
    print("Sauron has returned.")

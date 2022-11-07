p1,c1,p2,c2 = input().split()
if int(p1)*int(c1) < int(p2)*int(c2):
    print('1')
elif int(p1)*int(c1) == int(p2)*int(c2):
    print('0')
else:
    print('-1')

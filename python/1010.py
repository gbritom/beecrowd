x = input().split()
x = list(map(float, x))
y = input().split()
y = list(map(float, y))
sum = x[1]*x[2] + y[2]*y[1]
print("VALOR A PAGAR: R$ %.2f"%sum)

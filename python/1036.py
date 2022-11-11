import math
x = input().split()
x = list(map(float,x))
try:
    delta = (x[1]**2-(4*x[0]*x[2]))
    x1 = ((-1*x[1])+math.sqrt(delta))/(2*x[0])
    x2 = ((-1*x[1])-math.sqrt(delta))/(2*x[0])
    print("R1 = %.5f"%x1)
    print("R2 = %.5f"%x2)
except :
    print("Impossivel calcular")

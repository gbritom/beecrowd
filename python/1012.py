pi = 3.14159
x = input().split()
x = list(map(float,x))
print("TRIANGULO: %.3f"%((x[0]*x[2])/2))
print("CIRCULO: %.3f"%(pi*x[2]**2))
print("TRAPEZIO: %.3f"%((abs(x[0]+x[1])*x[2])/2))
print("QUADRADO: %.3f"%(x[1]**2))
print("RETANGULO: %.3f"%(x[0]*x[1]))

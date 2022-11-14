a = int(input())
print(a)
print(f"{int(a//100)} nota(s) de R$ 100,00")
a = a%100
print(f"{int(a//50)} nota(s) de R$ 50,00")
a = a%50
print(f"{int(a//20)} nota(s) de R$ 20,00")
a = a%20
print(f"{int(a//10)} nota(s) de R$ 10,00")
a = a%10
print(f"{int(a//5)} nota(s) de R$ 5,00")
a = a%5
print(f"{int(a//2)} nota(s) de R$ 2,00")
a = a%2
print(f"{int(a//1)} nota(s) de R$ 1,00")
a = a%1
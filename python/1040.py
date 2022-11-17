a,b,c,d = list(map(float,input().split()))
media = (2*a+3*b+4*c+d)/10
print(f"Media: {media:.1f}")
if media >= 5 and media<7:
    print("Aluno em exame.")
    e = float(input())
    print(f"Nota do exame: {e:.1f}")
    mf = (e+media)/2
    if  mf >= 5:
        print(f"Aluno aprovado.\nMedia final: {mf:.1f}")
elif media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")

pep = [300,1500,600,1000,150]
def soma (porcoes):
    var = 0
    for i in range(len(porcoes)):
        var+=porcoes[i]*pep[i]
    return var+225
    
porcoes=[] 
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
porcoes.append(a),porcoes.append(b),porcoes.append(c),porcoes.append(d),porcoes.append(e)
print(soma(porcoes))

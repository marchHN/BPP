import pdb
pdb.set_trace()

listaNumeros = [[2,4,1], [1,2,3,4,5,6,7,8], [100,250,43]]
listaMax = [max(l) for l in listaNumeros]
print(listaMax)

def esPrimo(n):
    primo = True
    for i in range(2, (n//2)+1):
        if(n%i == 0):
            primo = False
    return primo

listaNumeros = [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(esPrimo,listaNumeros))
print(primos)
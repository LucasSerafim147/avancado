numero = [0.0]*10
tam = len(numero)
cont = 0

for x in range (tam):
    numero[x] = int(input("Insira os numeros: "))
numeros = int(input("Insira um numero para comparar: "))

for i in range(tam):
    if numeros == numero[i]:
        cont += 1
print(numero,numeros,cont)



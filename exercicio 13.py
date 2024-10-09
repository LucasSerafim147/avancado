numeros = [0.0]*10
tam = len(numeros)
maior=0
menor=10000000000000000

soma = 0
for i in range(tam):
    numeros[i] = int(input("Insira os numeros: "))
print(numeros)
for x in range(tam):
    if numeros[x] % 2 == 0:
        print(numeros[x], end= " ")
for j in range(tam):
    soma += numeros[j]
media = soma/tam
for p in range(tam):
    if numeros[p] > media:
        print(numeros[p],end= " \n")
for m in range(tam):
    if numeros[m] > maior:
        maior = numeros[m]
    elif numeros[m] < menor:
        menor = numeros[m]
print(menor,maior)


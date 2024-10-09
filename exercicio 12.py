nomes = [""]*5
tam = len(nomes)

for i in range(tam):
    nomes[i] = input("Insira seus nomes: ")
print(nomes)
for x in range(tam-1,-1,-1):
    print(nomes[x])


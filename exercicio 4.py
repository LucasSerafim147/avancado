arrayNotas = [0.0]*5
tam= len(arrayNotas)
soma = 0
cont = 0
for x in range(tam):
    arrayNotas[x] = float(input("Insira notas: "))
for i in range(tam):
    soma += arrayNotas[i]
totalMedia = soma/tam
for o in range(tam):
    if arrayNotas[o] > totalMedia:
        cont += 1
print(f" a media da turma é {totalMedia} e {cont} alunso obtiveram a melhor nota")






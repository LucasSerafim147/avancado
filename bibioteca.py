from os import remove


def par(n):
    if n % 2== 0:
        print("o numero é par")
def impar(n):
    if n % 2 != 0:
        print("numero é impar")
def imprimir_nome(nome):
    print(f"olá : {nome}")
def piramide(n):
    for i in range(1,n+1):
        for x in range(i):
            print(i,end=" ", )
        print()
def piramide2(n):
    for i in range(1, n+1):
        for x in range(1,i+1):
            print(x, end=" ", )
        print()
def vogais(texto):
    tam = len(texto)
    cont = 0
    for i in range(tam):
        if texto[i]  in "aeiouAEIOU":
            cont += 1
            print(cont)
def numero(*n):
    soma = 0
    t=len(n)
    for i in n:
        soma += i

    print(soma)
def texto(texti):
    t = len(texti)
    cont = 0
    for i in texti:
        if i not in  " !@#$%&*":
            cont+=1
    print(cont)
    print(texti[::-1])
def lista():
    a = [10,12,12,31,4,4,5,31,6,7,6,8]
    nova = set(a)
    print(nova)






























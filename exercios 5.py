A= [0.0]*10
tam = len(A)
M= [0.0]*10


for i in range(tam):
    A[i] = int(input("Insira os numeros: "))
multi = int(input("Insira um numero para ser o multiplicador"))
for x in range(tam):
    M[x] = multi * A[x]
print(A, multi, M)







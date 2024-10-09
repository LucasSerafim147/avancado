nomes= [""]*5
senha = [000]*5

n=len(nomes)


for x in range(n):
    nomes[x] = input("Insira seu nome: ")
    senha[x] = int(input("Insira sua senha: "))
for j in range(n):
    print(f"o usuario {nomes[j]} tem a senha {senha[j]}e sua posição é {j}")



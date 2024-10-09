# Desafio menu login
nomes = [""]
senha = [000]
n = len(nomes)
tentativa = 0
while True:
    op = int(input(("Insira a opção desejada\n"
                    "1-Cadastro\n"
                    "2-Mostrar\n"
                    "3-Login\n"
                    "4-Sair\n")))

    if op == 1:
        for x in range(n):
            nomes_usuario = input("Insira seu nome: ")
            senha_usuario = int(input("Insira sua senha: "))

            nomes.append(nomes_usuario)
            senha.append(senha_usuario)
            print("O usuario foi cadastrado!  ")
    elif op == 2:
        print(f"usuarios cadastrados: {nomes}")

    # pedir login
    elif op == 3:
        tentativa = 0
        while tentativa < 3:

            login = input("Insira seu usuario: ")
            se = int(input("Insira sua senha: "))

            if login in nomes:
                i = nomes.index(login)
                if senha[i] == se:
                    print("Acesso garantido! ")
                    break
                else:
                    print("Senha incorreta!")
                    tentativa += 1
            else:
                print("Usuário não encontrado!")
                tentativa += 1

            if tentativa == 3:
                print("Número máximo de tentativas excedido. Tente novamente mais tarde.")
                break
        if op == 4:
            print("Saindo do Sistema")
            break










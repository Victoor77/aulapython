usuarios = []

def criar_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    localidade = input("Digite sua localidade: ")
    salario = float(input("Digite seu salário: "))

    usuario = {
        'nome': nome,
        'idade': idade,
        'localidade': localidade,
        'salario': salario
    }

    usuarios.append(usuario)
    print("Parabéns, seu usuário foi cadastrado com sucesso! \n")

def mostrar_usuarios():
    if not usuarios:
        print("Usuário não cadastrado. \n")
    else:
        for idx, usuario in enumerate(usuarios, start=1):
            print(f"\nUsuário {idx}:")
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Localidade: {usuario['localidade']}")
            print(f"Salário: {usuario['salario']}")
            print("-" * 30)

def main():
    while True:
        print("Menu de Navegação:")
        print("[1] Novo Cadastro")
        print("[2] Listar Usuários")
        print("[3] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_usuario()
        elif opcao == '2':
            mostrar_usuarios()
        elif opcao == '3':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
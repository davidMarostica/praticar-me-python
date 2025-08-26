# Projeto Prático 16: Registro de Atividades
# Descrição: Este programa permite que o usuário registre, visualize, 
# busque e exclua atividades ou notas em um arquivo de texto.

NOME_ARQUIVO = "atividades.txt"

# Adicionar atividade
def adicionar_atividades():
    atividade = input("Digite a atividade que deseja salvar no arquivo:")

    with open(NOME_ARQUIVO, "a") as arquivo:
        arquivo.write(atividade + "\n")
    print("Atividade registrada com sucesso!")    

def visualizar_atividades():
    try:
        with open(NOME_ARQUIVO, "r") as arquivo:
            atividades = arquivo.readlines()

            if atividades:
                print("=== Atividades Registradas===")
                for i, atividade in enumerate(atividades, start=1):
                    print(f"{i}. {atividade}")

            else:
                print("Nenhuma atividade registrada.")

    except FileNotFoundError:
        print("Nenhum atividade registrada ainda.")

     

# Buscar atividades
def buscar_atividade():
    termo = input("Digite o termo para buscar:")

    try:
        with open(NOME_ARQUIVO, "r") as arquivo:
            atividades = arquivo.readlines()

            resultados =[atividade.strip() for atividade in atividades if termo.lower() in atividade.lower()]

            if resultados:
                for i, resultado in enumerate(resultados, start=1):
                    print(f"{i}. {resultado}")

            else:
                print(f"Nenhuma atividae encontrada para o termo: {termo}")
           
    except FileNotFoundError:
        print("Nenhum atividade registrada ainda.")



# Excluir atividades
def excluir_atividade():
    visualizar_atividades()

    try:

        with open(NOME_ARQUIVO, "r") as arquivo:
            atividades = arquivo.readlines()


        if atividades:
           
           indice = int(input("Digite o número da atividade que deseja excluir:"))
           if 1 <= indice <= len(atividades):
               atividade_excluida = atividades.pop(indice - 1)
               with open(NOME_ARQUIVO, "w") as arquivo:
                    arquivo.writelines(atividades)

               print(f"Atividade {atividade_excluida} excluida com sucesso.")
           
           else:
            print("Número inválido. Nenhuma atividade foi excluida.")

        else:
            print("Nenhuma atividade encontrada ainda.")
        
    except FileNotFoundError:
        print("Nenhama atividade encontrada ainda.")
    except ValueError:
        print("Entrada inválida. Digite uma número válido.")


    


def meu_principal():

    while True:
        print("=== Menu Principal===")
        print("1. Adicionar nova atividade")
        print("2. Visualizar uma atividade ")
        print("3. Buscar uma atividade")
        print("4. excluir atividade")
        print("5. Sair")

        opcao = input("Escolha uma opição:")

        if opcao == "1":
           adicionar_atividades()
        elif opcao == "2":
           visualizar_atividades()
        elif opcao == "3":
            buscar_atividade()
        elif opcao == "4":
            excluir_atividade() 
        elif opcao == "5":
            print("Saindo do Programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente!")
            

if __name__=="__main__":
    meu_principal()
    


        


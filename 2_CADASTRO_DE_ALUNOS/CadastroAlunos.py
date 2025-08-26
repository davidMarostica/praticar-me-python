# Projeto Prático 18: Sistema de Cadastro de Alunos
# Descrição: Sistema que gerencia o cadastro de alunos utilizando uma classe Aluno. 
# Os alunos serão armazenados em uma lista para manipulação, como adição, visualização e busca.
import json

class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def __str__(self):
        return f"Matrícula: {self.matricula}, Nome: {self.nome}, Idade: {self.idade}"
    

class SistemaCadastro():
    def __init__(self):
        self.alunos = []
        self.carregar_de_arquivo()  # Carregar dados ao iniciar o sistema

    def cadastrar_aluno(self):
        nome = input("Digite o nome do aluno: ")
        idade = input("Digite a idade do aluno: ")
        matricula = input("Digite o numero de matricula do aluno: ")

        # Verificar se a matrícula já existe
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                print("Erro: Já existe um aluno com esta matrícula!")
                return

        aluno = Aluno(nome, idade, matricula)
        self.alunos.append(aluno)
        self.salvar_em_arquivo()  # Salvar após cadastrar
        print(f"Aluno {nome} adicionado com sucesso!")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno encontrado...")
        else:
            print("=== Lista de Alunos ===")
            for aluno in self.alunos:
                print(aluno)

    def buscar_aluno(self):
        matricula = input("Digite a matrícula do aluno que deseja encontrar: ")

        for aluno in self.alunos:
            if aluno.matricula == matricula:
                print("=== Aluno encontrado ===")
                print(aluno)
                return
        print("Aluno não encontrado!")
    
    def remover_aluno(self):
        matricula = input("Digite a matrícula do aluno que deseja remover: ")
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                self.salvar_em_arquivo()  # Salvar após remover
                print(f"Aluno {aluno.nome} removido com sucesso!")
                return
        print("Aluno não encontrado.")

    def salvar_em_arquivo(self):
        with open("alunos.json", "w", encoding="utf-8") as f:
            # Converter objetos Aluno para dicionários
            lista_alunos = [{"nome": aluno.nome, "idade": aluno.idade, "matricula": aluno.matricula} 
                           for aluno in self.alunos]
            json.dump(lista_alunos, f, ensure_ascii=False, indent=4)
    
    def carregar_de_arquivo(self):
        try:
            with open("alunos.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                for aluno_data in dados:
                    aluno = Aluno(aluno_data["nome"], aluno_data["idade"], aluno_data["matricula"])
                    self.alunos.append(aluno)
        except FileNotFoundError:
            # Arquivo não existe ainda, isso é normal na primeira execução
            pass
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

    def menu(self):
        while True:
            print("\n=== Menu Sistema de Cadastro ===")
            print("1. Cadastrar Aluno")
            print("2. Exibir Alunos")
            print("3. Buscar Aluno")
            print("4. Remover Aluno")
            print("5. Sair")

            opcao = input("Selecione uma opção: ")

            if opcao == "1":
                self.cadastrar_aluno()
            elif opcao == "2":
                self.listar_alunos()
            elif opcao == "3":
                self.buscar_aluno()
            elif opcao == "4":
                self.remover_aluno()
            elif opcao == "5":
                print("Saindo do Sistema...")
                break
            else:
                print("Opção inválida. Selecione de 1 a 5.")  


if __name__ == "__main__":
    sistema = SistemaCadastro()
    sistema.menu()
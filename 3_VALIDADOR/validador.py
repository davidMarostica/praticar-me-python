import re

def validar_email(email):
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(padrao, email):
        return True
    return False

def validar_telefone(telefone):
    padrao = r"^\(?\d{2,3}\)?[\s-]?\d{4,5}[\s-]?\d{4}$"
    if re.match(padrao, telefone):
        return True
    return False

def validar_cpf(cpf):
    # Primeiro valida o formato
    if not re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf):
        return False
    
    # Remove caracteres não numéricos
    numeros = re.sub(r"[^\d]", "", cpf)
    
    # Verifica se todos os dígitos são iguais (CPF inválido)
    if len(set(numeros)) == 1:
        return False
    
    # Validação dos dígitos verificadores
    def calcular_digito(digits, peso_inicial):
        soma = 0
        for i, digit in enumerate(digits):
            soma += int(digit) * (peso_inicial - i)
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    
    # Primeiro dígito verificador
    primeiro_digito = calcular_digito(numeros[:9], 10)
    if primeiro_digito != numeros[9]:
        return False
    
    # Segundo dígito verificador
    segundo_digito = calcular_digito(numeros[:10], 11)
    if segundo_digito != numeros[10]:
        return False
    
    return True

def validar_cep(cep):
    # Formato: 12345-678 ou 12345678
    padrao = r"^\d{5}-?\d{3}$"
    if re.match(padrao, cep):
        return True
    return False

def validar_cidade(cidade):
    # Nome de cidade válido: apenas letras, espaços e hífens, com pelo menos 3 caracteres
    padrao = r"^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\s-]{3,}$"
    if re.match(padrao, cidade) and len(cidade.strip()) >= 3:
        return True
    return False

def validar_estado(estado):
    # Lista de siglas de estados brasileiros válidos
    estados_brasileiros = [
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
        'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 
        'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    ]
    
    # Verifica se a sigla está em maiúsculas e é válida
    if estado.upper() in estados_brasileiros:
        return True
    return False

def formatar_telefone(telefone):
    """Função adicional para formatar telefone"""
    # Remove caracteres não numéricos
    numeros = re.sub(r"[^\d]", "", telefone)
    
    if len(numeros) == 11:
        return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"
    elif len(numeros) == 12:
        return f"({numeros[:3]}) {numeros[3:8]}-{numeros[8:]}"
    return telefone

def formatar_cep(cep):
    """Função para formatar CEP"""
    # Remove caracteres não numéricos
    numeros = re.sub(r"[^\d]", "", cep)
    
    if len(numeros) == 8:
        return f"{numeros[:5]}-{numeros[5:]}"
    return cep

def menu():
    while True:
        print("\n" + "="*40)
        print("          VALIDADOR DE DADOS")
        print("="*40)
        print("1. Validar E-mail")
        print("2. Validar Telefone")
        print("3. Validar CPF")
        print("4. Validar CEP")
        print("5. Validar Cidade")
        print("6. Validar Estado (UF)")
        print("7. Formatar Telefone")
        print("8. Formatar CEP")
        print("9. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            email = input("Digite o e-mail a ser validado: ").strip()
            if validar_email(email):
                print("✅ E-mail válido.")
            else:
                print("❌ E-mail inválido.")
                
        elif opcao == "2":
            telefone = input("Digite o telefone a ser validado: ").strip()
            if validar_telefone(telefone):
                print("✅ Telefone válido.")
            else:
                print("❌ Telefone inválido.")
                print("Formatos aceitos: (XX) XXXXX-XXXX, (XXX) XXXXX-XXXX, XX XXXXXXXX, etc.")
                
        elif opcao == "3":
            cpf = input("Digite o CPF a ser validado (formato: XXX.XXX.XXX-XX): ").strip()
            if validar_cpf(cpf):
                print("✅ CPF válido.")
            else:
                print("❌ CPF inválido.")
                print("Formato esperado: XXX.XXX.XXX-XX")
                
        elif opcao == "4":
            cep = input("Digite o CEP a ser validado: ").strip()
            if validar_cep(cep):
                print("✅ CEP válido.")
            else:
                print("❌ CEP inválido.")
                print("Formato esperado: XXXXX-XXX ou XXXXXXXX")
                
        elif opcao == "5":
            cidade = input("Digite o nome da cidade a ser validado: ").strip()
            if validar_cidade(cidade):
                print("✅ Nome de cidade válido.")
            else:
                print("❌ Nome de cidade inválido.")
                print("A cidade deve conter apenas letras, espaços e hífens, com pelo menos 3 caracteres.")
                
        elif opcao == "6":
            estado = input("Digite a sigla do estado (UF) a ser validada: ").strip()
            if validar_estado(estado):
                print(f"✅ {estado.upper()} é uma sigla de estado válida.")
            else:
                print("❌ Sigla de estado inválida.")
                print("Digite uma sigla válida de estado brasileiro (ex: SP, RJ, MG).")
                
        elif opcao == "7":
            telefone = input("Digite o telefone para formatar: ").strip()
            formatado = formatar_telefone(telefone)
            print(f"Telefone formatado: {formatado}")
            
        elif opcao == "8":
            cep = input("Digite o CEP para formatar: ").strip()
            formatado = formatar_cep(cep)
            print(f"CEP formatado: {formatado}")
            
        elif opcao == "9":
            print("Obrigado por usar o Validador de Dados. Até mais!")
            break
            
        else:
            print("❌ Opção inválida. Por favor, escolha uma opção entre 1 e 9.")

        # Pausa antes de limpar a tela e mostrar o menu novamente
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu()
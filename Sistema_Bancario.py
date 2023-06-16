import textwrap

def menu():
    menu = '''

================ MENU ================

-> [d]\tDeposito
-> [s]\tSacar
-> [e]\tExtrato
-> [nc]\tNova conta
-> [lc]\tListar contas
-> [nu]\tNovo usuário
-> [q]\tSair

======================================
    '''
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
    if valor > 0:    
        saldo = float(saldo + valor)
        extrato.append(f'\nDepósito:    R$ {valor:.2f}')
        print(f'\nO valor depositado foi de: R$ {float(valor):.2f}')
        print(f'\nValor atual: R$ {saldo:.2f}')
    else:
        print('\nO valor informado não pode ser depositado,\ntente novamente...')
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    

    if excedeu_saldo:
        print("\nOperação não realizada;\nVocê pode ter digitado um valor maior que o saldo atual da conta\ntente novamente...")

    elif excedeu_limite:
        print("\nOperação não realizada;\nO valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação não realizada;\nLimite de saques diario já realizado!")
        

    elif valor > 0:
        saldo -= valor
        extrato.append(f"\nSaque:       R$ {valor:.2f}")
        numero_saques += 1
        print(f'\nEm instantes o saque será realizado...\nNovo saldo: R$ {saldo:.2f}')
        print(f'Numero de saques: {numero_saques}')

    else:
        print("\nOperação não realizada;\nO valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibe_extrato(saldo, /, *, extrato):
    
    print("\n================ EXTRATO ================")
    if extrato:
         print(*extrato)
    else:
        print('\nNão foram realizadas movimentações.')        
    print(f'\nSaldo atual: R$ {saldo:.2f}')
    print("==========================================")

    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input('Informe o seu CPF:')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Usuario já existente com este CPF!')
        return
    nome = input('informe o nome completo:')
    data_nascimento = input('informe a data de nascimento (dd-mm-aaaa):')
    endereco = input('Informe o endereço (logradouro, n° - bairro - cidade/sigla estado):')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print('***Usuario criado com Sucesso!***')
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado,\nFluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
    
        opcao = menu()
    
        if opcao == 'd':
            valor = float(input('Informe o valor a ser depositado: '))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor a ser sacado: '))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            
            exibe_extrato(saldo, extrato=extrato)
   
        elif opcao == 'q':
             print('Obrigado por usar nossos serviços, até logo!')
             break
        
        elif opcao == 'nc': #Nova Conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc': #Lista conta
            listar_contas(contas)
        
        elif opcao == 'nu': #Novo usuário
            criar_usuario(usuarios)
        
        else:
             print('Operação invalida!\nTente novamente...')
main()
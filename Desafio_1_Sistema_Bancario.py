menu = '''

Escolha uma das opções abaixo, para realizar sua operação:

-> [d] Deposito
-> [s] Sacar
-> [e] Extrato
-> [q] Sair

 '''
saldo = 0
limite = 500
extrato = []
extrato_final = []
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == 'd':
        deposito = 0
        deposito = float(input('Informe o valor a ser depositado: '))
        if deposito > 0:    
            extrato.append(f'Depósito: R$ {deposito:.2f}')
            saldo = float(saldo + deposito)
            extrato_final.append((f'R$ {saldo:.2f}'))
            print(f'\nO valor depositado foi de: R$ {float(deposito):.2f}')
            valor_final = extrato_final[-1]
            print(f'\nValor atual: {valor_final}')
        else:
             print('\nO valor informado não pode ser depositado,\ntente novamente...')
             

    
    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
                saque = 0
                saque = float(input('Informe o valor a ser sacado: '))
                if saque <= saldo and saque <= limite and saque > 0:
                    extrato.append(f'Saque:    R$ {saque:.2f}')
                    saldo = float(saldo - saque)
                    print(f'\nEm instantes o saque será realizado...\nNovo saldo: R$ {saldo:.2f}')
                    numero_saques = numero_saques + 1
                else:
                    print('\nOperação não realizada;\nVocê pode ter digitado um valor maior que o saldo atual da conta ou um valor acima de 500 R$;\nConsulte seu saldo atual ou tente novamente...')
        else:
            print('Limite de saques diario já realizado!') 

    elif opcao == 'e':

        print('\n>>>>>>>>>>>>>Extrato<<<<<<<<<<<<<')
        if extrato:
             print(*extrato, sep = '\n')
        else:
            print('\nNão foram realizadas movimentações.')        
        print(f'\nSaldo atual: R$ {saldo:.2f}')
        print('>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<')


    elif opcao == 'q':
         print('Obrigado por usar nossos serviços, até logo!')
         break

    else:
         print('Operação invalida!\nTente novamente...')
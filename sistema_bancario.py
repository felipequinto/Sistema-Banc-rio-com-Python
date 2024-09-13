# Menu de opçoes do sistema
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

# Inicialização das variáveis
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal para execução contínua até o usuário escolher sair
while True:
    opcao = input(menu).lower() # Solicita a opção e converte para minúsculo

    if opcao == 'd': #Opção de depósito
        try:
            valor = float(input('Informe o valor do depósito: '))
        
            if valor > 0:
                saldo += valor # Adiciona o valor ao saldo
                extrato += f'Depósito de R$ {valor:.2f}\n' # Registra o depósito no extrato
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
            else:
                print('Operação falhou! O valor informado é inválido.')
        
        except ValueError:
            print('Valor inválido! Informe um número válido.')
        
    elif opcao == 's': # Opção de saque
        try:
            valor = float(input('Informe o valor do saque: '))

            # Verificações de restrições para saque
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print('Operação falhou! Você não tem saldo suficiente.')

            elif excedeu_limite:
                print('Operação falhou! O valor do saque excede o limite.')

            elif excedeu_saques:
                print('Operação falhou! Número máximo de saques excedido.')
                
            elif valor > 0:
                saldo -= valor # Deduz o valor do saldo
                extrato += f'Saque: R$ {valor:.2f}\n' # Registra o saque no extrato
                numero_saques += 1 # Incrementa o contador de saques
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            else:
                 print('Operação falhou! O valor informado é inválido.')

        except ValueError:
            print('Valor inválido! Informe um número válido.')

    elif opcao == 'e': # Opção de extrato
        print('\n================ EXTRATO ================')
        # Exibe extrato ou mensagem de que não há movimentações
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('==========================================')

    elif opcao == 'q':  # Opção de sair
        print('Obrigado por utilizar nossos serviços. Até logo!')
        break  # Encerra o loop

    else:
        print('Operação inválida! Por favor, selecione uma operação válida.')
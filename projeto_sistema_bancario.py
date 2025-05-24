menu = """
Selecione a opção desejada:
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
quantidade_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1": 
       print("""Você selecionou a opção de depósito. 
             
             Aguarde
             
             """)
       
       valor_deposito = float(input(f"Insira o valor para depósito:\n"))

       if valor_deposito <= 0:
             print("Erro. Insira um valor válido para depósito.")

       if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Você depositou o valor de: R${valor_deposito:.2f}")
            
    
    elif opcao == "2":
        
     if saldo <= 0:
       print("Você não possui saldo suficiente para sacar.")
       
     elif saldo > 0:
        print("""Você selecionou a opção de saque.
          Observação: você possui um limite de 3 saques diários.
              
              Aguarde
              
              """)
        valor_saque = float(input(f"\nInsira o valor que você deseja sacar: \n"))

        if valor_saque < 0:
             print("Erro. Insira um valor válido para sacar.")

        elif valor_saque > saldo:
             print("Você não possui saldo suficiente para sacar este valor.")    
        
        elif quantidade_de_saques >= LIMITE_SAQUES:
             print("Você excedeu o número máximo de saques diário.")
        
        elif valor_saque > limite:
             print("Você excedeu o limite de R$500,00 de saque diário.")
        
        elif valor_saque <= saldo:
             quantidade_de_saques += 1
             saldo -= valor_saque
             extrato += f"Saque: R$ {valor_saque:.2f}"
             
             print(f"\nVocê sacou o valor de: R${valor_saque:.2f}")
    
    elif opcao == "3":
         print("\n================ EXTRATO ================")
         print("Não foram realizadas movimentações na conta." if not extrato else extrato)
         print(f"\nSaldo: R$ {saldo:.2f}")
         print("==========================================")

    elif opcao == "4":
        break


    else:
        print("Operação inválida, por favor selecione novamente a operação de desejada.")

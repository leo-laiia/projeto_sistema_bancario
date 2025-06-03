import pytz
from datetime import datetime, timedelta

menu = """
\tSelecione a opção desejada:
\t[1] Depositar
\t[2] Sacar
\t[3] Extrato
\t[4] Sair

=> """
# Declarando a função para coletar a data/hora da transação realizada.
def horario_transacao():
    data_transacao = datetime.now(pytz.timezone("America/Sao_Paulo"))
    dia_seguinte = (data_transacao + timedelta(days=1)).replace(hour=0, minute=0)
    return data_transacao, dia_seguinte # Retornando as variáveis da função para poderem ser utilizadas no restante do código.

# Declarando uma variável que recebe a variável "data_transacao" da função. Mantive o mesmo nome pra ficar mais fácil de lembrar. 
data_transacao, _ = horario_transacao() # O underline "_", nesse caso serve para ignorar o(s) outro(s) valore(s) retornados na função.
_, dia_seguinte = horario_transacao() # Declarando uma variável que recebe a variável "dia_seguinte" da função. Mesma ideia da função de cima.

saldo = 0
limite_valor_saque = 500
extrato = ""
saques = 0
transacoes = 0
LIMITE_SAQUE = 3

while True:
    # Declarando a função para passar um parâmetro de limite de transações gerais diárias. 
    def LIMITE_TRANSACOES():
         LIMITE_TRANSACOES = 10
         excedeu_limite_transacoes = data_transacao < dia_seguinte and transacoes >= LIMITE_TRANSACOES # Declarando a variável que passa os parâmetros para que o limite de transaçõs seja excedido. 
         # A variável recebe os dados coletados da data/hora da trasação realizada, quantas vezes as transações foram realizadas e os parâmetros de comparação para serem validados posteriormente.
         return excedeu_limite_transacoes # Retornando o valor que será passado ao chamar a função LIMITE_TRANSACOES(). Nesse caso não achei necessário usar a ideia de declarar uma variável recebendo o valor retornado.
     
    opcao = input(menu)

    if opcao == "1":
        # Condições e lógica if/else/elif para validar os requistos necessários de operações no menu.
        if LIMITE_TRANSACOES():
              print("\n\tVocê excedeu o limite de transações permitidas diariamente.")  
              
        elif LIMITE_TRANSACOES() is False: # Achei interessante testar o uso prático do operador "is".
              print("""\n\tVocê selecionou a opção de depósito. 
                 
                    Aguarde
                 """)
              valor_deposito = float(input(f"\n\tInsira o valor para depósito:\n"))
              transacoes += 1
              saldo += valor_deposito
              extrato += f"\tDepósito: R$ {valor_deposito:.2f} [Horário da transação realizada: {data_transacao.strftime("%d/%m/%Y %H:%M")}]\n"
              print(f"\n\tVocê depositou o valor de: R${valor_deposito:.2f}")
            
    elif opcao == "2":    
         
         if saldo <= 0:
              print("\n\tVocê não possui saldo suficiente para sacar.")
       
         if LIMITE_TRANSACOES():
              print("\n\tVocê excedeu o limite de transações permitidas diariamente.")
     
         elif saldo > 0:
              print("""\n\tVocê selecionou a opção de saque.
                    Aguarde
                    """)
              valor_saque = float(input(f"\n\tInsira o valor que você deseja sacar: \n"))
              excedeu_limite_saques = saques > LIMITE_SAQUE
              excedeu_valor_saque = valor_saque > limite_valor_saque
              saldo_insuficiente = valor_saque > saldo                       
              
              if valor_saque < 0:
                   print("\n\tErro. Insira um valor válido para sacar.")
               
              elif saldo_insuficiente:
                   print("\n\tVocê não possui saldo suficiente para sacar este valor.")    
               
              elif excedeu_limite_saques:
                   print("\n\tVocê excedeu o número máximo de saques diário.")
          
              elif excedeu_valor_saque:
                   print("\n\tVocê excedeu o valor limite para sacar.")
        
              elif valor_saque <= saldo:
                  transacoes += 1
                  saques += 1
                  saldo -= valor_saque
                  extrato += f"\tSaque: R$ {valor_saque:.2f} [Horário da transação realizada: {data_transacao.strftime("%d/%m/%Y %H:%M")}]\n"
                  print(f"\n\tVocê sacou o valor de: R${valor_saque:.2f} ")
    
    elif opcao == "3":
         print("\n================ EXTRATO ================")
         print("\tNão foram realizadas movimentações na conta." if not extrato else extrato)
         print(f"\nSaldo: R$ {saldo:.2f}")
         print("==========================================")

    elif opcao == "4":
        break


    else:
        print("\tOperação inválida, por favor selecione novamente a operação desejada.")

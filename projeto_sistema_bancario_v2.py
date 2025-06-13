import pytz, textwrap
from datetime import datetime, timedelta
# trocar function LIMITE_TRANSACOES
menu = """
  Selecione a opção desejada:
  [1]\tDepositar
  [2]\tSacar
  [3]\tExtrato
  [nc]\tNova Conta
  [lc]\tListar contas
  [nu]\tNovo usuário
  [Q]\tSair
   => """

def horario_transacao():
    data_transacao = datetime.now(pytz.timezone("America/Sao_Paulo"))
    dia_seguinte = (data_transacao + timedelta(days=1)).replace(hour=0, minute=0)
    
    return data_transacao, dia_seguinte # Retornando as variáveis da função para poderem ser utilizadas no restante do código.

data_transacao, _ = horario_transacao() 
_, dia_seguinte = horario_transacao() 

def deposito(saldo, valor, extrato, limite_transacoes):
    
      if limite_transacoes <= 0 and data_transacao < dia_seguinte:
        print("\n\tVocê excedeu o limite de transações permitidas diariamente.")   

      elif valor > 0:
         limite_transacoes -= 1
         saldo += valor
         extrato += f"\tDepósito: R$ {valor:.2f} [Horário da transação realizada: {data_transacao.strftime("%d/%m/%Y %H:%M")}]\n"
         print(f"\n\tVocê depositou o valor de: R${valor:.2f}")
         print(saldo, limite_transacoes)

      if valor < 0:
       print("Erro. Insira um valor válido para depósito.")
      
      return saldo, extrato, limite_transacoes
     
def saque(*, saldo, valor, extrato, limite_valor_saque, saques, limite_transacoes, LIMITE_SAQUE):      
     excedeu_limite_saques = saques > LIMITE_SAQUE
     excedeu_valor_saque = valor > limite_valor_saque
     saldo_insuficiente = valor > saldo 
    
     if saldo <= 0:
        print("\n\tVocê não possui saldo suficiente para sacar.")
     
     elif valor <= 0:
        print("\n\tErro. Insira um valor válido para sacar.")  
        
     elif limite_transacoes <= 0 and data_transacao < dia_seguinte:
        print("\n\tVocê excedeu o limite de transações permitidas diariamente.")

     elif saldo > 0:  
  
      if saldo_insuficiente:
          print("\n\tVocê não possui saldo suficiente para sacar este valor.")    
               
      elif excedeu_limite_saques:
          print("\n\tVocê excedeu o número máximo de saques diário.")
          
      elif excedeu_valor_saque:
          print("\n\tVocê excedeu o valor limite para sacar.")
      elif valor <= saldo and valor > 0:
          transacoes -= 1
          saques += 1
          saldo -= valor
          extrato += f"\tSaque: R$ {valor:.2f} [Horário da transação realizada: {data_transacao.strftime("%d/%m/%Y %H:%M")}]\n"
          print(f"\n\tVocê sacou o valor de: R${valor:.2f} ")
        
     return saldo, extrato, limite_transacoes

def imprimir_extrato(saldo, /, *, extrato):
     print("\n================ EXTRATO ================")
     print("\tNão foram realizadas movimentações na conta." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("==========================================")
    
     return saldo, extrato

def criar_usuario(usuarios):
   cpf = input("Insira o seu CPF (somente números): \n") #CPF possui 11 dígitos
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print("\n@@@ Já existe usuário com esse CPF! @@@")
      return
     
   nome = (input(f"Insira o seu nome:\n"))
   data_nascimento = input(f"Insira a sua data de nascimento no formato ''DD-MM-AAAA'' Exemplo: 5/5/2000:\n")
   conv_date = datetime.strptime(data_nascimento, '%d/%m/%Y') 
   conv_date.date()
   d = conv_date.strftime('%d/%m/%Y')
    
   endereco = (input(f"Insira o seu endereço no formato logradouro, número, bairro, cidade, sigla estado. Exemplo: Rua Um, nro 2, bairro três, Rio de Janeiro, RJ:\n"))
     
   usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
   print("\t Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
   return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
   cpf = input("Informe o CPF do usuário: ")
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print("\n=== Conta criada com sucesso! ===")
      return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

   #print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
   for conta in contas:
        linha = f""" 
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
   AGENCIA = "0001"
   LIMITE_SAQUE = 3
   
   saldo = 0
   limite_valor_saque = 500
   extrato = ""
   saques = 0
   limite_transacoes = 10 
   usuarios = []
   contas = []    
   
   while True:
        opcao = input(menu)

        if opcao == "1":
            print("""\n\tVocê selecionou a opção de depósito. 
             Aguarde
             """)
            valor = float(input(f"\n\tInsira o valor para depósito:\n"))
            
            saldo, extrato, limite_transacoes = deposito(
                saldo, 
                valor, 
                extrato, 
                limite_transacoes
            )

        elif opcao == "2":    
            print("""\n\tVocê selecionou a opção de saque.
                  Aguarde
                  """)
            valor = float(input(f"\n\tInsira o valor para saque:\n"))
            
            saldo, extrato, limite_transacoes = saque(
                saldo=saldo,
                valor=valor, 
                extrato=extrato,
                limite_valor_saque=limite_valor_saque,
                saques=saques, 
                limite_transacoes=limite_transacoes,
                LIMITE_SAQUE = LIMITE_SAQUE
            )

        elif opcao == "3":
           imprimir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "Q":   
           break
        
        else:
           print("\tOperação inválida, por favor selecione novamente a operação desejada.")

main()
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        
        print("Depósito")
        valor_deposito = float(input("Qual valor do depósito? "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        
        else:
            print("Operação falhou! Valor informado é inválido!")
        
    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Qual o valor do saque?"))
        if numero_saques >=LIMITE_SAQUES:
            print("Seus saques diários se esgotaram")
        elif valor_saque > limite:
            print("Seu limite de saque é R$ 500,00")
        
        elif valor_saque > saldo:
            print ("Saldo insuficiente")
            
        elif valor_saque <= saldo and valor_saque <= limite and numero_saques <= LIMITE_SAQUES:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            
        else:
            print("Operação falhou, tente novamente!")
        
        
    elif opcao == "e":
      print("\n=========== Extrato ===========")
      print("Não foram realizadas movimentações" if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("==================================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
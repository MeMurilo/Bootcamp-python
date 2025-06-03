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
        
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Verifique os números informados e o saldo de sua conta.")

    elif opcao == "s":
        
     
      valor = float(input("Informe o valor do saque: "))
      
      execedeu_valor = valor > saldo
      excedeu_limite = valor >= limite
      excedeu_saque = numero_saques >= LIMITE_SAQUES
      
     
          
      if execedeu_valor:
        print("Você não possui esse saldo na conta.")
        
      if excedeu_limite:
        print("Valor limite de saque atingindo.")
        
      if excedeu_saque:
         print("Número de saques maximos atingido")
         
         
        
      elif valor > 0:
        saldo -= valor
        numero_saques +=1
        extrato += f"Saque: R$ {valor:.2f}\n"
             
                   
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    
    elif opcao =="q":
        print("Obrigado por acessar nosso banco!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
             
       
             
    
    
        
   
    
     

   
      
        
     
       
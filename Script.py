senha = "1234"
contador = 3
Saldo = 0.0

while contador > 0:
    tentativa = input("Digite a sua senha! ")
    
    if tentativa != senha:
        print("SENHA INVÁLIDA")
        contador -= 1
        if contador == 0:
            print("O SISTEMA ENCERROU POR EXCESSO DE 3(TRÊS) TENTATIVAS DE ACESSO INVÁLIDOS")
            break
            
    elif tentativa == senha:
        print("\n Acesso Permitido")
        
        while True:
            print("\n--- MENU ---")
            print("1 - Ver Saldo")
            print("2 - Depósito")
            print("3 - Saque")
            print("0 - Sair")
                
            op = input("Digite um numero entre 0-3 \n")
     
            match(op):
                case "1":
                    print(f"Seu Saldo bancário é de: R${Saldo:.2f}")
                
                case "2":
                    deposito = float(input("Deseja fazer o depósito de quanto: R$"))
                    if deposito > 0:
                        Saldo += deposito
                        print("DEPÓSITO REALIZADO COM SUCESSO")
                    else:
                        print("Digite um número positivo")
                    
                case "3":
                    Saque = float(input("Deseja sacar quanto: R$"))
                    if Saque > Saldo:
                        print("SALDO INSUFICIENTE PARA SAQUE")
                    elif Saque > 0:
                        Saldo -= Saque 
                        print("SAQUE REALIZADO COM SUCESSO") 
                    else:
                        print("Ocorreu um erro tente Novamente")
                                
                case "0":
                    print("Saindo do menu...")
                    break 
                
                case _:
                    print("Opção inválida!")
                    break
# Armazenar os investimentos
investments = []

# verifica os múltiplos de 2, 3 ou 5
def is_valid_parcel(parcel):
    return parcel % 2 == 0 or parcel % 3 == 0 or parcel % 5 == 0

# Função para adicionar um novo investimento
def add_investment():
    amount = float(input("Informe o valor do investimento: "))
    parcel = int(input("Informe o número de parcelas para pagamento (múltiplo de 2, 3 ou 5): "))
    
    if not is_valid_parcel(parcel):
        print("O número de parcelas deve ser múltiplo de 2, 3 ou 5.")
        return
    
    investment_type = int(input("Escolha o tipo de investimento: 1 para CDB, 2 para LCI, 3 para LCA: "))
    investments.append({"type": investment_type, "amount": amount})
    print("Investimento adicionado com sucesso!")

# Função para realizar o resgate de um investimento
def redeem_investment():
    if not investments:
        print("Nenhum investimento para resgate.")
        return
    
    investment_type = int(input("Informe o tipo de investimento para resgate (1 para CDB, 2 para LCI, 3 para LCA): "))
    amount_to_redeem = float(input("Informe o valor a ser resgatado: "))
    days_invested = int(input("Informe o número de dias que o valor permaneceu investido: "))
    
    # Procurar o investimento do tipo solicitado
    for inv in investments:
        if inv["type"] == investment_type:
            if inv["amount"] >= amount_to_redeem:
                tax = 0
                if investment_type == 1:  # CDB possui imposto
                    if days_invested <= 180:
                        tax = 0.225
                    elif days_invested <= 360:
                        tax = 0.20
                    elif days_invested <= 720:
                        tax = 0.175
                    else:
                        tax = 0.15
                    tax_amount = amount_to_redeem * tax
                    amount_after_tax = amount_to_redeem - tax_amount
                else:  # LCI e LCA são isentos de IR
                    amount_after_tax = amount_to_redeem
                
                inv["amount"] -= amount_to_redeem
                if inv["amount"] <= 0:
                    investments.remove(inv)  # Remove o investimento se o saldo for zero
                
                print(f"Resgate realizado! Valor após IR: R${amount_after_tax:.2f}")
                return
            else:
                print("Saldo insuficiente para o resgate.")
                return
    print("Investimento não encontrado para o resgate.")

# Função principal
def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Realizar investimento")
        print("2. Realizar resgate")
        print("3. Sair")
        
        choice = int(input("Escolha uma opção: "))
        
        if choice == 1:
            add_investment()
        elif choice == 2:
            redeem_investment()
        elif choice == 3:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa principal
main()

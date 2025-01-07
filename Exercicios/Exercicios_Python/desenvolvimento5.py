escolha = 1

while (escolha != 0):
    print("""
        ============== Calculadora ==========
        1: Soma
        2: Subtração
        3: Multiplicação
        4: Divisão
        0: Sair
        =====================================
        """)
    escolha = int(input("Escolha uma opção: "))
    
    if (escolha == 0):
        print("Obrigado por usar a calculadora!")
    elif (escolha > 4 or escolha < 0):
        print("Opção inválida. Por favor, tente novamente.")
    else:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
    
        if escolha == 1:
            print(f"A soma de {num1} e {num2} é {num1 + num2}")
        elif escolha == 2:
            print(f"A subtração de {num1} e {num2} é {num1 - num2}")
        elif escolha == 3:
            print(f"A multiplicação de {num1} e {num2} é {num1 * num2}")
        elif escolha == 4:
            print(f"A divisão entre {num1} e {num2} é {num1 / num2}")
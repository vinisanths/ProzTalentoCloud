numeroCerto = False
while(numeroCerto == False):
    print("Digite um numero Par: ")
    try:
        numero = int(input())
        if(numero % 2 ==0):
            numeroCerto = True
            print(f"O numero {numero} é par")
        else:
            print(f"O numero {numero} não é par")
    except:
        print("Digite um numero valido")
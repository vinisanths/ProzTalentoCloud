def calculadora(num1, num2, operador):
    if operador == 1:
        return num1 + num2
    elif operador == 2:
        return num1 - num2
    elif operador == 3:
        return num1 * num2
    elif operador == 4:
        return num1 / num2
    else:
        return "Operador invalido"
    
resultado = calculadora(5,2,1)
print(resultado)
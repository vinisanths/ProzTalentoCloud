#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


anoCerto = False
anoAtual = 2024
nome = str(input("Digite seu nome completo: "))
while(anoCerto == False):
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        if(ano_nascimento >= 1922 and ano_nascimento <= 2025):
            idade = anoAtual - ano_nascimento
            print(f"Olá {nome}, você tem {idade} anos")
            anoCerto = True
    except:
        print("Digite um ano válido")
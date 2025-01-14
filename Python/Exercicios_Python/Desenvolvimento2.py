quantiRodas = int(input("Informe a quantidade de Rodas: "))
print(quantiRodas)
pesoBruto = float(input("Informe o peso bruto: "))
print(pesoBruto)
quantiPessoas = int(input("Informe a Quantidades de pessoas no veiculo: "))
print(quantiPessoas)
if (quantiRodas >= 4 and pesoBruto > 6000):
    print("Categoria Recomendada: E")
elif(quantiRodas >= 4 and quantiPessoas > 8):
  print("Categoria Recomendada: D")
elif(quantiRodas >= 4 and pesoBruto >= 3500 and pesoBruto <=6000):
  print("Categoria Recomendada: C")
elif(quantiRodas >= 4 and quantiPessoas <= 8 and pesoBruto <= 3500):
  print("Categoria Recomendada: B")
else:
  print("Categoria Recomendada: A")
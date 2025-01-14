nomes = ["Rafael", "Arturo", "Karen", "Julia"]

def acharElemento(item, lista):
 itemEncontrado = False
 indiceItem = 0
 
 for i in range(len(lista)):
    if (lista[i] == item):
      itemEncontrado = True
      iItem = i 

 if (itemEncontrado):
  print(f"O item {item} foi no indice {i} encontrado")
 else:
  print(f"O item {item} não foi encontrado")

acharElemento("Julia", nomes)

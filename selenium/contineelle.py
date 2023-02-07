""" 
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [2, 3, 4, 5, 6, 99, 100]
listavacia =[]

for i, elemento in enumerate(lista2):
    if elemento in lista1:
        index = lista1.index(elemento)
        siguientes_lista1 = lista1[index+1:index+6]
        siguientes_lista2 = lista2[i+1:i+6]
        siguientes_lista2 += [0] * (5 - len(siguientes_lista2))
        if siguientes_lista1 == siguientes_lista2:
            print(f"Los siguientes 5 elementos de {elemento} son iguales en ambas listas")
        else:
            print(f"Los siguientes 5 elementos de {elemento} no son iguales en ambas listas")
            listavacia.append(elemento)
    else:
        print(f"El elemento {elemento} no está en la lista 1")
        listavacia.append(elemento)

print(f" final {listavacia}") """

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [2, 3, 4, 5, 6, 7, 100,5,6,9,32,34,2,3,6,7]
listavacia=[]

i = 0
while i < len(lista2):
    elemento = lista2[i]
    if elemento in lista1:
        index = lista1.index(elemento)
        siguientes_lista1 = lista1[index+1:index+6]
        siguientes_lista2 = lista2[i+1:i+6]
        siguientes_lista2 += [0] * (5 - len(siguientes_lista2))
        if siguientes_lista1 == siguientes_lista2:
            #print(f"Los siguientes 5 elementos de {elemento} son iguales en ambas listas")
            i += 6
        else:
            #print(f"Los siguientes 5 elementos de {elemento} no son iguales en ambas listas")
            i += 1
            listavacia.append(elemento)
    else:
        #print(f"El elemento {elemento} no está en la lista 1")
        i += 1
        listavacia.append(elemento)

print(listavacia)
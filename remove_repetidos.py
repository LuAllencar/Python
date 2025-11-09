def remove_repetidos(lista):
    lista_nova = list(dict.fromkeys(lista))
    lista_nova.sort()
    return lista_nova

lista = []
remove_repetidos(lista)
print(remove_repetidos(lista))
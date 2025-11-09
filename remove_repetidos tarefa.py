def remove_repetidos(lista):
    lista_nova = list(dict.fromkeys(lista))
    lista_nova.sort()
    return lista_nova

lista = []

while True:
    elemento = input("Digite um elemento para adicionar à lista (ou 'sair' para finalizar): ")
    if elemento.lower() == 'sair':
        break
    elemento = int(elemento)  # Convertendo para inteiro
    lista.append(elemento)

remove_repetidos(lista)
print(remove_repetidos(lista))
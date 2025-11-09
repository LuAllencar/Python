def maior_elemento(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

lista = []
print(maior_elemento(lista))
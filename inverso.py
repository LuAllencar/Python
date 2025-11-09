def inverso(lista):
    nova_lista = lista[::-1]
    return nova_lista

lista = []
elemento = 1
while True:
    elemento = int(input("Digite um número: "))
    if elemento == 0:
        break
    lista.append(elemento)

for elemento in inverso(lista):
    print(elemento)

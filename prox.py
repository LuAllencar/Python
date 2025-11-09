lista=[]
maior=float('-inf')
menor=float('inf')
while True:
    dado=int(input("Digite um número para acrescentar na lista: "))
    if dado==0:
        break
    lista.append(dado)
    if dado>maior:
        maior=dado
    if dado<menor:
        menor=dado

print("\nLista completa:", lista)
print("A quantidade de elementos é:",len(lista))
print("O maior número da sequência é:",maior)
print("O menor número da sequência é:",menor)
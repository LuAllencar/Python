contador = 0

while True:
    print("Contador atual:", contador)
    escolha = input("Digite 'i' para incrementar ou 's' para sair: ").lower()

    if escolha == 'i':
        contador += 1
        continue
    elif escolha == 's':
        print("Você encerrou com o contador em:", contador)
        break
    else:
        print("Opção inválida. Tente novamente.")
        continue

# Agora usamos range(0, n+1) com o valor final do contador
print("\nContando de 0 até", contador)
for i in range(0, contador + 1):
    print(i, "  ", end="")

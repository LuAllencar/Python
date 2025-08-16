# Declara uma matriz vazia
matriz = []

# para o índice 'linha', que se repete 3 vezes.
# abrimos o índice 'coluna', que se repete 4 vezes e o valor vem da leitura do cliente!

for i in range(3):
    linha = [] # criamos uma linha vazia!
    for j in range(4):
        valor = int(input(f"Digite um valor para a posição [{i}][{j}] na matriz: "))
        linha.append(valor) # append pega o valor digitado e coloca dentro da linha vazia
    matriz.append(linha) # append pega a linha já completa e acrescenta na matriz!

# Mostrando objeto em cada posição específica
print("\nMatriz:")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Elemento na posição: ({i}, {j}): {matriz[i][j]}")

# maior valor da matriz!!!
maior = max(max(linha) for linha in matriz)
print(f"\nO maior valor da matriz é: {maior}")

# menor valor da matriz!!!
menor = min(min(linha) for linha in matriz)
print(f"O menor valor da matriz é: {menor}")


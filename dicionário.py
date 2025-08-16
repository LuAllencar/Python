
listaProdutos = []
itens = 0

while True or range(5):
    produto = {}
    produto["Id"] = input("Digite o ID do produto: ")
    produto["Nome"] = input("Digite o nome do produto: ")
    produto["Preço"] = float(input("Digite o preço do produto: "))
    listaProdutos.append(produto)

    # Exibindo os dados do produto
    # Quantidade de produtos cadastrados!!!
    itens += 1
    print(f"\nQuantidade de produtos cadastrados: {itens}")
    print(f"ID: {produto['Id']}, Nome: {produto['Nome']}, Preço: {produto['Preço']}")
    
    # a parte do texto .lower() converte a resposta do usuário para minúsculas
    # assim, se o usuário digitar 'S' ou 's', o programa continuará
    # se digitar 'N' ou 'n', o programa irá parar
    continuar = input("Deseja cadastrar outro produto? (s/n): ").lower()

    # a lógica foi, se a resposta for diferente de 's', o loop irá parar
    if continuar != 's':
        break

    

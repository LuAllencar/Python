largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

def retangulo(altura, largura):
    while altura > 0 and largura > 0:
        print("#" * largura)
        altura -= 1
        while altura >= 2 and largura >= 2:
            print("#" + " " * (largura - 2) + "#")
            altura -= 1

retangulo(altura, largura)

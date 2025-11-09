largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

def retangulo(altura, largura):
    while altura > 0 and largura > 0:
        print("#" * largura)
        altura -= 1
        
print()
retangulo(altura, largura)

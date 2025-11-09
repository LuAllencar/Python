a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

def maximo(a, b):
    while a>b:
        return (f">>> maximo ({a}, {b})")
    while b>a:
        return (f">>> maximo ({b}, {a})")
print(maximo(a, b))
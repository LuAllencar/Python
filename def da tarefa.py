# # def multiplica (a, b):
# #     return a * b

# # print(multiplica(4,5))

# def troca(x, y):
#     aux = x
#     x = y
#     y = aux

# x = 10
# y = 20
# troca (x,y)
# print("x =", x,"e y =",y)



# def total_Caracteres(x, y, z):
#     return len(x) + len(y) + len(z)
# print(total_Caracteres("Luana", "Gomes", "de Souza"))

# a = int(input("Digite o primeiro número: "))
# b = int(input("Digite o segundo número: "))

# def maximo(a, b):
#     while a>b:
#         return (f">>> maximo ({a}, {b})")
#     while b>a:
#         return (f">>> maximo ({b}, {a})")
# print(maximo(a, b))


x = input("Digite uma letra: ")
def vogal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return bool(True)
    else:
        return bool(False)
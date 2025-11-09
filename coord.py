import math

x1 = int(input("Digite o primeiro valor de x: "))
y1 = int(input("Digite o primeiro valor de y: "))

x2 = int(input("Digite o segundo valor de x: "))
y2 = int(input("Digite o segundo valor de y: "))

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if dist>=10:
	print("longe")
else:
	print("perto")
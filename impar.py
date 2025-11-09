n = int (input("Digite o valor de n: "))
impar = 1
aux=0

while n != aux:
	if impar % 2 != 0:
		print(impar)
		impar=impar+1
		aux=aux+1
	else:
		impar=impar+1
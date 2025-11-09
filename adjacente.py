n = input("Digite um número inteiro: ")

i=0
achou=False

while i < len(n)-1:
	if n[i] == n[i+1]:
		achou = True
		break
	i = i+1
if achou:
	print("sim")
else:
	print("não")
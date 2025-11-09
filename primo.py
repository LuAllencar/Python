n=int(input("Digite um número inteiro: "))

if n<2:
	print("não primo")
else:
	i=2
	primo=True
	while i<n:
		if n % i ==0:
			primo=False
			break
		i=i+1
	if primo:
		print("primo")
	else:
		print("não primo")
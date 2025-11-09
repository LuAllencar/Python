n = int(input("Digite um número inteiro: "))
alg=0
soma=0

while n>0:
	alg=(n%10)
	soma=soma+alg
	n=(n//10)
print(soma)
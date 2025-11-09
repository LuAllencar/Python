n = int (input("Digite o valor de n: "))
aux=0
multi=1

if n==0 or n==1:
	print("1")
else:

	while n > 1:
		multi=multi*n
		n=n-1
	print(multi)
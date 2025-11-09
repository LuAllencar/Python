segundosrec=int(input("Qual é o valor, em segundos, que deseja converter? "))
dias = segundosrec // 86400
horas = (segundosrec % 86400) // 3600
minutos = ((segundosrec % 86400)%3600)//60
segundos = (((segundosrec % 86400)%3600)%60)

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
#Reescreva seu programa de pagamento, para pagar ao funcionário 1.5 vezes o valor da taxa horária de pagamento pelo tempo
#trabalhado acima de 40 horas
hour=float(input('Quantas horas?'))
hourly_rate=float(input('Quanto você recebe por hora trabalhada?'))
pay= hourly_rate * hour
if hour <= 40:
    print(pay)
elif hour > 40:
    print(hourly_rate * 40 + (hour - 40) * hourly_rate * 1.5)
else:      
        print("enter a number")
#Reescreva seu programa de pagamento utilizando try e
#except, de forma que o programa consiga lidar com entradas não numéricas graciosamente, mostrando uma mensagem e saindo do programa. A
#seguir é mostrado duas execuções do programa
try:
    hour=float(input('Quantas horas?'))
    hourly_rate=float(input('Quanto você recebe por hora trabalhada?'))
    pay= hourly_rate * hour
    if hour <= 40:
        print(pay)
    elif hour > 40:
        print(hourly_rate * 40 + (hour - 40) * hourly_rate * 1.5)
    else:      
            print("enter a number")
except ValueError:
    print ("por favor utilize uma entrada numérica")
    quit()
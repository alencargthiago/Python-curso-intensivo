hour=float(input('Quantas horas?'))
hourly_rate=float(input('Quanto você recebe por hora trabalhada?'))
pay= hourly_rate * hour
if hour <= 40:
    print(pay)
elif hour > 40:
    print(hourly_rate * 40 + (hour - 40) * hourly_rate * 1.5)
else:      
        print("enter a number")


def counterpay(hours, rate):
    if hours <=40:
        pay= hours * rate
    else:
        pay= 40 * rate + (hours -40) * rate * 1.5
    return pay
hours=float(input("Quantas horas trabalhadas?"))
rate=float(input("Quaal a taxa recebida por hora trabalhada?"))

total_pay= counterpay(hours, rate)
print("Pay:", total_pay)
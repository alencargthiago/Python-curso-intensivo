#Escreva um programa que solicite ao usuário as horas e o
#valor da taxa por horas para calcular o valor a ser pago por horas de
#serviço.
hour= float(input("Quantas horas você trabalha?"))
hourly= float(input("Quantos você ganha por hora trabalhada?"))
pay= hour * hourly
print ("Pay:", pay)

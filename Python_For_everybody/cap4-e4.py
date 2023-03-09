#  Reescreva seu programa de cálculo de pagamento com um
# 1.5 o valor de hora de trabalho por hora extra, crie uma função chamada
# calculoPagamento que aceita dois parâmetros(horas e TaxaHora).

#a saída deve conter:

# Insira as Horas: 45
# Insira o valor da Hora de Trabalho: 10
# pagamento: 475.0


def calculoPagamento (horas, taxa_hora):
    if horas <= 40:
        pay= horas * taxa_hora
    else: pay= 40 * taxa_hora + (horas-40) * taxa_hora * 1.5
    return pay

horas=float(input("insira as horas?"))
taxa_hora=float(input("insira o valor da hora de trabalho?"))
total_pay=calculoPagamento(horas, taxa_hora)
print ("Pagamento:",total_pay)
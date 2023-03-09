# Reescreva o programa de notas do capítulo anterior usando a função computarNotas que recebe a pontuação como parâmetro e
# retorna a nota como uma string.

# Pontuação Nota
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Insira a pontuação: 0.95
# A

# Insira a pontuação: perfeito
# Pontuação Inválida
# Insira a pontuação: 10.0
# Pontuação Inválida
# Insira a pontuação: 0.75
# C
# Insira a pontuação: 0.5
# F
# Execute o programa repetitivamente para testar vários valores diferentes como
# entrada

def computar_nota (nota):
    try:
        if nota >= 0.9:
            nota_abc="A"
        elif nota>= 0.8:
            nota_abc= "B"
        elif nota >=0.7:
            nota_abc= "C"
        elif nota >=0.6:
            nota_abc="D"
        else: 
            nota_abc="F"
        return nota_abc
    except:
        print("Pontuação inválida")
try:       
    nota=float(input("Insira sua nota"))
    print_nota = computar_nota(nota)
    print("Sua nota é:", print_nota)
except:
    print("Pontuação inválida")
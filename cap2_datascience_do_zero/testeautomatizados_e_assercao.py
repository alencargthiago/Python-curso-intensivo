def soma(a,b):
    return a+b
#teste
resultado= soma(2,3)
assert resultado ==5, f"esperado:5, obtido: {resultado}"

resultado2= soma(-2, 2)
assert resultado2== 0, f"esperado 0, obtido {resultado2}"

resultado3= soma(0,0)
assert resultado3 == 0, f"esperado 0, obtido {resultado3}"

print(resultado)
print(resultado2)
print(resultado3)
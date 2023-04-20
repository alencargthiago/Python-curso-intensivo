def aplicar_funcao(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def soma(a, b):
    return a + b

def saudacao(nome, sobrenome, titulo="Sr."):
    return f"{titulo} {nome} {sobrenome}"

# Usando aplicar_funcao para chamar a função soma com argumentos posicionais
resultado_soma = aplicar_funcao(soma, 1, 2)
print(resultado_soma)  # Saída: 3

# Usando aplicar_funcao para chamar a função saudacao com argumentos posicionais e de palavra-chave
resultado_saudacao = aplicar_funcao(saudacao, "João", "Silva", titulo="Dr.")
print(resultado_saudacao)  # Saída: "Dr. João Silva"
# Algoritmo para validar a força de uma senha.

# Input da senha
senha = str(input("Digite sua senha: "))
minuscula = maiuscula = digito = especial = 1

# Condicional do tamanho da senha
if len(senha) > 5:
    tamanho = 0
    print('Sua senha possui pelo menos 6 caracteres')
else:
    tamanho = 6-len(senha)
    print('Sua senha não possui pelo menos 6 caracteres')

# Condicionais para validar demais critérios
for i in senha:
    if i in "abcdefghijklmnopqrstuvxz" and minuscula != 0:
        minuscula = 0
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and maiuscula != 0:
        maiuscula = 0
    if i in "!@#$%^&*()-+" and especial != 0:
        especial = 0
    if i in "0123456789" and digito != 0:
        digito = 0

# Testes para ajudar o usuário a melhorar sua senha
if minuscula == 0:
    print('Sua senha possui pelo menos uma letra minúscula')
else:
    print('Sua senha não possui pelo menos uma letra minuscula')

if maiuscula == 0:
    print('Sua senha possui pelo menos uma letra maiúscula')
else:
    print('Sua senha não possui pelo menos uma letra maiúscula')

if especial == 0:
    print('Sua senha possui pelo menos um caracter especial')
else:
    print('Sua senha não possui pelo menos um caracter especial')

if digito == 0:
    print('Sua senha possui pelo menos um digito numérico')
else:
    print('Sua senha não possui pelo menos um digito numérico')

# Se falta atender "tamanho" mais do que as demais #condições, output "tamanho"
# Caso contrário, output é a quantidade de critérios faltantes
if tamanho > minuscula+maiuscula+especial+digito:
    print(f'Faltam {tamanho} caracteres')
elif minuscula+maiuscula+especial+digito > tamanho:
    print(f'Faltam {minuscula+maiuscula+especial+digito} caracteres')
else:
    print('Senha forte')

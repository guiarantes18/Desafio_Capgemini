# Algoritmo para validar a força de uma senha.

# Input da senha
senha = str(input())

# Quantidade mínima de caracteres necessários para cada condição
minuscula = maiuscula = digito = especial = 1

# Condicional para validar o tamanho da senha
if len(senha) > 5:
    tamanho = 0
else:
    tamanho = 6-len(senha)

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

# Se falta atender "tamanho" mais do que as demais #condições, output "tamanho"
# Caso contrário, output é a quantidade de critérios faltantes
if tamanho > minuscula+maiuscula+especial+digito:
    print(tamanho)
else:
    print(minuscula+maiuscula+especial+digito)

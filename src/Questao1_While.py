# Algoritmo para imprimir uma escada de n degraus

# Input da quantidade de degraus. Valor numérico
n = int(input("n = "))
i = 1

# Output da escada com n degraus
while i <= n:
    print(" "*(n-i), "*"*i)
    i += 1

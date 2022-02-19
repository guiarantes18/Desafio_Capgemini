# Algoritmo para imprimir uma escada de n degraus

# Input da quantidade de degraus. Valor numérico
n = int(input("n = "))

# Output da escada com n degraus
for i in range(1, n+1):
    print(" "*(n-i), "*"*i)

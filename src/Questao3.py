# Algoritmo para verificar se as substrings de uma palavra são anagramas entre si

# Leitura da String e transforma todas as letras maiusculas em minusculas
palavra = str(input()).lower()

# Contador de anagrama encontrados
cont = 0

# Variável k auxilia na quantidade de letras a ser analisada a cada iteração e no tamanho/quantidade
# de iterações
# Variavel i auxilia na navegação das primeiras letras da palavra digitada
# Variavel j auxilia na navegação das ultimas letras da palavra
# Organiza-se em ordem alfabética crescente os caracteres de cada grupo de letras analisado e
# compara-os para verificar se é um possível anagrama
for k in range(1, len(palavra)):
    for i in range(0, len(palavra)-k):
        for j in range(i+1, len(palavra)+1-k):
            aux1 = "".join(sorted(palavra[i:i+k]))
            aux2 = "".join(sorted(palavra[j:j+k]))
            if aux1 == aux2:
                cont += 1
print(cont)

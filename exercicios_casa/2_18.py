# Escreva um programa que solicite ao usuário frases.
# Para parar de solicitar frases, ele pede apenas apertar o "enter".
# Seu  programa deve apresentar cada frase e quantas vezes ela foi repetida.

dados = {}

while True:
    frase = input("Entre com a frase:")
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

# posso usar assim for i, j in dados.items():
    #print(i, "->", j) ou...

for i in dados:
    print(i, "->", dados[i])

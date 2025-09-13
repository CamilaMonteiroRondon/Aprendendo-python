#%%
nome = "Camila"

# For sempre vai pecorrer os elementos de algum objeto.
for letra in nome:
    print(letra)

#%%

numero = 2
max_numero = 100

# range cria uma sequencia de numero.

for i in range(1, max_numero+1):
    print(numero, "x", i, "=", numero * i)

#%%
# Quais números sõa divisiveis por 4 no intervalo [4-100].

for i in range(4, 101):
    if i % 4 == 0:
        print(i)
#%%
# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.


soma = 0 # valor final
qtde_entradas = 4 # o contador de entradas

for i in range(qtde_entradas): # mesma coisa que range(0, 4) ou range(0, qtde_entradas)

    altura = input("Entre com a altura:")
    altura = float(altura)
    soma += altura
    qtde_entradas -= 1

print("Soma das alturas:", soma)

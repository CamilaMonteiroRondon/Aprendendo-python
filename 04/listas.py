#%%
# lista é um conjunto de elememntos.
# exemplo abaixo de uma maneira de definir listas.
idades =[28, 42, 43, 35, 39, 28, 38]
print(idades)

#%%
# listas em python nao sao arrays.

Camila = ["Camila", "solteira", 32, 1]
print(Camila)

type(Camila)
#%%
# saber a idade pegando o elemento (indice)
print(Camila[2])

print(Camila[0])

# %%
idades =[28, 42, 43, 35, 39, 28, 38, 42]

#somando as idades.
print("soma idades:", sum(idades))


# Len vai informar a quatidade de elementos na lista.
print("qtde idades:", len(idades))

# media das idades.
print("media idades:", sum(idades)/len(idades))

# menor idade.
print("menor idade:", min(idades))

# max idade.
print("maior idade:", max(idades))


# %%

Camila = ["Camila", 
          "Solteira", 
          32, 
          True, 
          ["Biologa", "Tec de laboratorio", "Professora"], 
          ["2000", "1900", "400"], 
          ["Alan", "Eduardo", "Matheus"]]

print("Tamanho de Camila", len(Camila))

print(Camila[6][0])

exs = Camila[6]
primeiro_ex = exs[0]
print(primeiro_ex)
# %%
# quero saber minha ultima lista e ultimo nome dessa lista.
tamanho = len(Camila)

pos = tamanho -1
exs = Camila[pos]

Camila[pos][len(exs)-1]

# %%
# saber minha ultima lista e ultimo nome de um outro jeito.
Camila[-1][-1]

# %%
# fatiamento 
# primeiros 4 elementos.
Camila[0:4]

# %%

Camila[4][1:3]

# %%

Camila[4][-2:]

# %%

Camila[:4]

# %%
# quer dizer que é da onde começa e onde termina. start primeiro elemento, stop final.
# Camila[ start : stop ]

# %%
Camila = ["Camila", 
          "Solteira", 
          32, 
          True, 
          ["Biologa", "Tec de laboratorio", "Professora"], 
          ["2000", "1900", "400"], 
          ["Alan", "Eduardo", "Matheus"]]
salarios = Camila[5]
print(salarios)
salarios[::-3]

# esta saltando de dois em dois.
# Camila[start:stop:step]
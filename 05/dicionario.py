# para acessar a lista se usa o indice. Variavel[].

#%%
# dicionarios são pares de chave/valor. a chave corresponde a um valor.
# {chave:valor}

dados_camila = {"nome": "camila", 
                "sobrenome":"monteiro", 
                "filhos":True,
                "formacao":["biologia", "tecnica de laboratorio"],
                "cargos":[{"nome":"coletora", "empresa":"sao franciso"},
                           {"nome":"tecnica de analises", "empresa":"upa"},
                           {"nome":"tecnica de laboratorio", "empresa":"upa"},
                           {"nome":"triagem/auxiliar", "empresa":"laudmed"},
                           
                ]
}

#%%

# para acessar o valor da chave é so passa o nome do valor.
print(dados_camila)
print(dados_camila["formacao"][-1])
print(dados_camila["cargos"][-1]["empresa"])

# as chaves pode ser string, inteiro e floot(evite pois nunca foi visto usando).
# mas pode ser qualquer tipo.

#%%

dados_camila["estado civil"] = "solteira"
 #%%

print(dados_camila)

#%%

print(dados_camila.keys())
print(dados_camila.values())
print("items", dados_camila.items())


#%%
#for i in dados_camila:
    #print(i,"->", dados_camila[i])
    
for chave, valor in dados_camila.items():
    print(chave,"->", valor)
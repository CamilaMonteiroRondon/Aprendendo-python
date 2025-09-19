#%%

nome_arquivo = "historia.txt"

# Essas duas linhas faz a mesma coisa que as que estão mais abaixo.
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)


# Abre arquivo em formato de leitura.
#open_file = open(nome_arquivo)

# Lê os dados do arquivo.
#conteudo = open_file.read()

#print(conteudo)

# Fecha o arquvio.
#open_file.close()


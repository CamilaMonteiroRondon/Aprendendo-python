#%%

import requests # para realizar requisições na web.
import json # para tratar listas/dicionários para arquivos JSON.
from tqdm import tqdm

import pandas as pd

# %%
ceps = [
    "26291368",
    "20010020",
    "20010060",
    "20010100",
]

url = "https://viacep.com.br/ws/{cep}/json/"
dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())
        
dados
#%%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep = ";")
# %%

with open("ceps.json","w", encoding= 'utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)



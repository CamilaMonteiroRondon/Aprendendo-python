#%%
# Quais números sõa divisiveis por 4 no intervalo [4-100].
# no lugar de count pode usar o i.
count = 4 #count também pode ser qualquer nome além do i.
while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)

    count += 1
    
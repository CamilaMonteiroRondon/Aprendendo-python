#%%
idade = 70

if idade >= 70:
    print("Cuidado com a bebida.")
    print("Consulte o seu geriatra!")

#booleando.
# o elif nasce apartir do if.

elif idade >= 18: #condição lógica.
    print("Você pode beber cerveja!")
    print("Beba com moderação!")
#repara que a condição foi verdadeira pois tem idade para beber.

else: #será só executado se o if ou elif for falso.
    print("Você não pode beber!")
    print("Vá para casa beber leite!")

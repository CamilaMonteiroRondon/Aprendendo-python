# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

fruta = input("Entre com o nome da fruta:")

frutas = {
    "Maçã": "R$1,50",
    "Banana": "R$2,75",
    "Uva": "R$1,90",
    "Pera": "R$1,25",
    "Laranja": "R$0,66",
    "Limão": "R$1,75",
    "Goiaba": "R$2,15",
    "Abacaxi": "R$3,20",
    "Jaca": "R$5,80",
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um valor válido!")
    
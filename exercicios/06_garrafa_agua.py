# Faça um programa que vende uma garrafa de água:
# se o cliente escolher água mineral natural, será cobrado R$1,50.
# se o cliente escolher água mineral com gás, será cobrado R$2,50.

texto = """ 
Escolha a sua água para comprar:
(1) Àgua mineral natural
(2) Àgua mineral com gás"""

opcao = input(texto)

if opcao == "1":
    print("Sua conta deu: R$1,50")

elif opcao == "2":
     print("Sua conta deu: R$2,50")

else:
    print("Entre com a opção correta, por favor.")

# OU
# opcao = input(texto)
# conta = 0
# if opcao == "1":
#   conta = 1.5
# elif opcao == "2"
#   conta = 2.5
# if conta == 0:
#   print("Entre com a opção correta, por favor.")
# else:
#   print("Sua conta é: R$:", conta)

#Pode fazer assim:

#def par_impar(numero:int):
    #if numero % 2 == 0:
        #print("È par!")
    #else:
        #print("È impar!")


#numero = input("Entre com um número:")
#numero = int(numero)

#par_impar(numero)

# Ou assim:

def par_impar(numero:int):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
numero = input("Entre com um número:")
numero = int(numero)

resultado = par_impar(numero)

print("O valor", numero, "é", resultado)
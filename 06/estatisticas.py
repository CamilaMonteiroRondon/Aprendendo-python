def soma(a:float, b:float, *args)->float:
    valores = [a,b] + list(args)
    return sum(valores)

# Argumentos opcionais so pode vim depois dos obrigatórios.
# args é uma convençao podendo ter so um com asterisco e pode por qualquer nome.
def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args)+2)

a = float(input("Entre com o valor de a:"))
b = float(input("Entre com o valor de b:"))
c = float(input("Entre com o valor de c:"))

print("Média:", media(a,b, c))
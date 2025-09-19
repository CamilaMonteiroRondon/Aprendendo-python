#%%

A = 1
B = 5

print(A) 
print(B)

# %%

C = A
A = B
B = C
print(A) 
print(B)

# %%

A,B = B,A
print(A) 
print(B)
# %%
# TUPLA?

B,A = A,B
# %%

# unpack descomprime a lista/tupla e mais de um elemeto.
a, b, *resto = 1,2,3,4,5,6,5,4,3,7,8
print(a, b, resto)
# %%

*resto, a, b = 2,3,4,5,6,7,8,4
print(a, b, resto)
# %%

a, *resto, b = 1,2,4,5
print(a, b, resto)
# %%

# o *args faz exatamente isso.

def soma(a, *args):
    total = a + sum(args)
    return total

soma(1,2,4,7)
# %%

def soma_quatro(a,b,c,d):
    return a+b+c+d
values = [1,2,3,4]
soma_quatro(*values)
# %%

soma(*values)
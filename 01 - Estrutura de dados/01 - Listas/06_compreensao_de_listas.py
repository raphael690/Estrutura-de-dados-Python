# Compreensão de listas -> oferece uma sintaxe mais curta quando você deseja: Criar um nova lista com base nos valores
# de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

print(""" ----------------filtrar lista (filtro versao2)-----------------""")

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


print(""" ----------------Modificar valores -----------------""")

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

print(""" ----------------Modificar valores versão 2-----------------""")

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero **2)
print(quadrado)
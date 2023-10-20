
# issubset -> é quando um determinado conjunto_a pertence ao conjunto_b ou vice-versa

conjunto_a = {1, 2, 3}
conjunto_b = { 4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)
print(resultado)
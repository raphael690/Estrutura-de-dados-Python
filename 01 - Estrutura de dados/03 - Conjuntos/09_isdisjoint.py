
# isdisjoint -> onde o conjunto não tem relação com o outro conjunto, os elemento ficam cada um em seu lugar.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = { 6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)
print(resultado)
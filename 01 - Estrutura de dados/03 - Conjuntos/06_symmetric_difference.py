
# mostrar todos os elementos que não estão na intercessão ou seja não se tocam.

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)

texto = input("Informe um texto: ")
#texto = ""
vogais = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end = " ")
else:
    print() # adiciona uma quebra de linha


    # Exemplo utilizando a função built-in range
    for numero in range(0,51, 5):
        print(numero, end= " ")
  
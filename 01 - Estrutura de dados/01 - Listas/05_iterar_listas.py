# Iterar listas -> A forma mais comum para percorrer os dados de uma lista é utilizando o comando (FOR)

carros = ["gol","celta","palio"]

for carro in carros:
    print(carro)

print("""------------------ Outra alternativa de efetuar o comando agora com a função enumerate -------------""")
# Função enumerate -> Às vezes é necessário saber qual o índice do objeto dentro do laço (for). Para isso podemos usar
# a função enumerate.
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
     
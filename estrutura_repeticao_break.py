#while True: # laço infinito
#    numero = int(input("Informe um número: "))

#    if numero == 10:
#        break

#    print(numero)

                            # Ha uma Variação do Break que é o continue
for numero in range(100):

    if numero % 2 == 0:
       continue

    print(numero, end=" ")

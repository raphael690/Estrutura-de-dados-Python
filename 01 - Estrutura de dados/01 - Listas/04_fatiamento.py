# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passa o índice
# inicial e/ ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso

lista = ["p","y","t","h","o","n"]

print(lista[2:])   #["t","h","o","n"]
print(lista[ :2])  #["p","y"]
print(lista[1:3])  #["y", "t"]
print(lista[0:3:2])#["p","t"]
print(lista[ : :]) #["p","y","t","h","o","n"]
print(lista[::-1]) #["n","o","h","t","y","p"]
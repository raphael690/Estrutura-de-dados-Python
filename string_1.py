curso = "pYtHon"

print(curso.upper()) # upper converter todos os caracteres para maiusculos

print(curso.lower()) # lower converter todos os caracteres para minusculos

print(curso.title()) # title converter todos os caracteres para minusculos exceto a primeira letra que ficará maiúsculo
"\n"
# Eliminando espaços em branco

texto = "  Olá mundo    "

print(texto + ".")

print(texto.strip() + ".") # strip remove os espaços em branco da esquerda e da direita

print(texto.rstrip() + ".") # rstrip remove os espaços em branco da direita

print(texto.lstrip() + ".") # lstrip remove os espaços em branco da esquerda

"\n"
# Junções e centralização de Strings

menu = "Programacao"

print("####" + menu + "####")

print(menu.center(10, "#")) # centralizar

print("-".join(menu)) # juntar os caracteres desejados

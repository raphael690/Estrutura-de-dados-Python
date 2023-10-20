# Metodo da classe dict
# Get -> é uma segunda forma de acessar valor dentro do dicionario.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

#contatos["chaves"] #keyError

resultado = contatos.get("chaves") #None
print(resultado)

resultado = contatos.get("carro") #{}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone":"3333-2221"}}
print(resultado)
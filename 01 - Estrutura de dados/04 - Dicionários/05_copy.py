# Método copy -> faz uma copia do nosso dicionário, utilizo quando não desejo alterar a chave original

contatos = {
    "guilherme@mail.com":{"nome":"Guilherme", "telefone":"3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"]= {"nome": "Gui"}

print(contatos["guilherme@mail.com"]) #{"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"]) #{"nome": "Gui"}
# Metodo da classe dict
# del-> outra forma de tirar o valor, irei passar o objeto que irei remover


contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
print(contatos)

print("=" * 100)

del contatos["chappie@gmail.com"]
print(contatos)

print("=" * 100)
#se colocar o comando abaixo apaga o dicionario inteiro

# Metodo da classe dict
# update -> atualizar o diconario com outro dicionario

contatos = {"Guilherme@gmail.com": {"nome": "guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com":{"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
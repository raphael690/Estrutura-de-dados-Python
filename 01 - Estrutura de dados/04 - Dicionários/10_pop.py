# Metodo da classe dict
# pop -> irá remover uma chave do seu dicionário e mostra o que foi removido

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com") # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {}) #{}
print(resultado)
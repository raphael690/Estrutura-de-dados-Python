# Metodo da classe dict
# keys -> retorna somente a chave do nosso dicionario util para saber quantas chaves tem o seu dicionario

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys() # dict_keys(['guilherme@gmail.com'])
print(resultado)


novo_dicionario = {"a": 100, 1:"teste", "b": "python"}
print(novo_dicionario.keys())

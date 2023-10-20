# Metodo da classe dict
# setdefault -> colocar um valor dentro do dicionario caso ele não exista.

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

#contato.setdefault("nome", "Giovanna") # "Guilherme"
#print(contato) #{'nome': 'Guilherme', 'telefone': '3333-2221}

contato.setdefault("idade", 28) # 28
print(contato) # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
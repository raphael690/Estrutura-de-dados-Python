# Metodo da classe dict
# popitem -> retira os item na seguencia, caso não tenha mais item a ser removido da a mensagem KeyError

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem() # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

#contatos.popitem() # KeyError

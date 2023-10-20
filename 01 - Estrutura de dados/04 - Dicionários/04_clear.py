# Método da classe dict
# Clear -> pelo comando contatos.clear()apaga todos valor do dicionario

contatos = {
    "guilherme@mail.com":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com":{"nome":"Gioavanna", "telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine", "telefone":"3333-7766"},
}

contatos.clear()
print(contatos) #{}
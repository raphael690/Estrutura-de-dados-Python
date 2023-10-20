
contatos = {
    "guilherme@mail.com":{"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com":{"nome":"Gioavanna", "telefone":"3443-2121"},
    "chappie@gmail.com":{"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com":{"nome":"Melaine", "telefone":"3333-7766", "extra":{"a": 1}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)

extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)
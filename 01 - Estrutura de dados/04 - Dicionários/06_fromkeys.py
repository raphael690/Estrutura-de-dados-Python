# Fromkeys -> é utilizado para criar chaves no dicionario e colocar ali , outra é criar um conjunto padrão
#nela

resultado = dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome","telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

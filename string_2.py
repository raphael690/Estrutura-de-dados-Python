nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" %(nome, idade)) # primeira forma %

print("Nome: {} Idade: {}".format(nome, idade)) # segunda forma com Format {}

print("Nome: {1} Idade: {0}".format(idade, nome)) # segunda forma com Format passando o indice {indice}
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome)) # segunda forma com Format  com repetição

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome)) # segunda forma é passando ele nomeado e em qualquer ordem
print("Nome: {nome} Idade: {idade}".format(**dados)) # segunda forma é definida por um dicionario **dados

print(f"Nome: {nome} Idade: {idade}") # Terceira Forma é pelo F-String no inicio
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}!") # Terceira Forma é Formatar strings com f-string
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")


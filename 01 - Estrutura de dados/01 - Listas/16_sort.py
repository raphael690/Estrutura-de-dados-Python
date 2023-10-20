# ---------------- Metodo sort organizar por ordem alfabetica ---------------------------#

print("""==================ordem alfabetica=================""")

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["python", "js", "c", "java", "csharp"]
print(linguagens)

print("""==========inverter a ordem ===========""")

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]

print("""==========len do menor para o maior ===========""")

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]
print(linguagens)

print("""==========len do menor para o maior reverse ===========""")

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]
print(linguagens)
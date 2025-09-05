"""Exercícios de manipulação de arquivos."""
# Manipulação de arquivos
nomes = ["Ana", "Bruno", "Carlos"]
with open("nomes.txt", "w", encoding="utf-8") as f:
    for nome in nomes:
        f.write(nome + "\n")
with open("nomes.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)

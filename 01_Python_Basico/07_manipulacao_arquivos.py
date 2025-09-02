# Manipulação de arquivos
"""Exercícios de manipulação de arquivos."""
# Exercício 1: Escreva uma lista de nomes em um arquivo txt
nomes = ["Ana", "Bruno", "Carlos"]
with open("nomes.txt", "w") as f:
    for nome in nomes:
        f.write(nome + "\n")

# Exercício 2: Leia o arquivo e imprima o conteúdo
with open("nomes.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

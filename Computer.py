import os
os.system('cls') or None

computer_pieces = ["i5 10th", "16GB ram"] #Lista com peças de um computador

#Add peças ao computador
computer_pieces.insert(0, "SO: Win10") # insert() add um item em um determinado indice
computer_pieces.append("RTX 3090") # append() add um item ao final da lista
computer_pieces.append("HD de 1TB")
computer_pieces.append("Mesa")
computer_pieces.append("Cadeira")

#Juntandos periféricos ao computador
peripherals = ["Monitor LG", "Teclado Logitech", "Mouse Multilaser"]

computer_pieces.extend(peripherals)

# Removendo coisas que não são peças de computador
computer_pieces.remove("Mesa") # remove() exclui um item especifico
computer_pieces.remove("Cadeira")

# 2 formas de exibir a lista
for y in computer_pieces:
    print(y)

#[print(z) for z in computer_pieces] #compreensão de lista









# @autora= Rayssa Pimenta !!
#Curso de Python da plataforma alura 


print ("*********************************")
print ("Bem Vindo ao jogo de advinhação !")
print ("*********************************")

numero_secreto = 42
numero_tentativas = 5

while (numero_tentativas > 0):
    chute_str = input ("Digite um número: ")
    chute = int (chute_str)
    print ("Você digitou: ", chute)

    acertou = numero_secreto == chute
    menor = chute < numero_secreto
    maior = chute > numero_secreto
    if (acertou):
        print ("Parabéns, você acertou!")
    elif (menor):
        print ("Ops, você errou! O número digitado é menor do que o esperado.")
    elif (maior):
        print ("Ops, você errou! O número digitado é maior do que o esperado.")
    numero_tentativas = numero_tentativas - 1
    print ("Você ainda tem ", numero_tentativas, " tentativas.")
print ("Fim de jogo !")
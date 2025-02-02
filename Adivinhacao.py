from random import randint

# print("*************************************")
# print("* Bem vindo ao jogo de adivinhação! *")
# print("*************************************")

# numero_secreto = 33

#chute_str = input("Digite o seu número: ")
#chute = int(chute_str)
# chute = int(input("Digite o seu número: "))
#
# if numero_secreto == chute:
#     print("Parabéns! Você acertou o número secreto!!!!!")
# else:
#     print("Você errou o número secreto!!!!!!")
#
# print("\n* Fim da rodada! *")

#Constantes
# numero_secreto = randint(0,100)
# rodada = 1

# while rodada <= 5:
#     # print("\n" + str(rodada) + "ª tentativa")
#     print("{} tentativa". format(rodada))
#     chute = int(input("Digite um número: "))
#     acertou = chute == numero_secreto
#     maior = chute > numero_secreto
#     menor = chute < numero_secreto
#
#     if acertou:
#         print('Parabéns, você acertou o número secreto!!!')
#     elif maior:
#         print('O número que você chutou é maior que o número secreto.')
#     # else: Se não quiser usar a variável menor
#     elif menor:
#         print('O número que você chutou é menor que o número secreto.')
#
#     rodada = rodada + 1
#     if rodada > 5:
#         print("O número gerado foi " + str(numero_secreto) + ".")
#         print("O jogo terminou. Tente outra vez!")

def jogar():
    print("*************************************")
    print("* Bem vindo ao jogo de adivinhação! *")
    print("*************************************")
    rodada = 1
    numero_tentativas = 0
    limite_menor = 1
    limite_maior = 100
    numero_secreto = 32
    contador = 0
    nivel = 0
    pontos = 1000
    pontos_perdidos = 0

    while contador < 1:
        print('\n Escolha o nível de dificuldade: \n(1) Fácil (2) Médio (3) Difícil')
        try:
            nivel = int(input('Digite o número: '))
            if nivel == 1:
                numero_tentativas = 10
                break
            elif nivel == 2:
                numero_tentativas = 5
                break
            elif nivel == 3:
                numero_tentativas = 3
                break
            else:
                print('Por favor, digite um número válido.')
                continue
        except ValueError:
            print('Esse não é um número válido.')
            print('Por favor, escolha um número válido entre 1 a 3.')


    # Loop
    for rodada in range(1, numero_tentativas + 1):
        print('{}ª tentativa de {}'.format(rodada,numero_tentativas))
        try:
            palpite = int(input('Digite um número entre {} e {}: '.format(limite_menor, limite_maior)))
        except ValueError:
            print("Ops! Você não digitou um número válido. Tente novamente!\n")
            continue

        # Variáveis
        maior = palpite > numero_secreto
        menor = palpite < numero_secreto

        # Condição errada
        if (palpite < limite_menor or palpite > limite_maior):
            print('O número escolhido não está entre {} e {}'.format(limite_menor, limite_maior) + '.\n')
            continue

        # Condição correta
        if maior:
            print('O número escolhido é maior que o número secreto!\n')
            pontos_perdidos = abs(palpite - numero_secreto) // 3
            pontos = pontos - pontos_perdidos
        elif menor:
            print('O número escolhido é menor que o número secreto!\n')
            pontos_perdidos = abs(palpite - numero_secreto) // 3
            pontos = pontos - pontos_perdidos
        else:
            print('Parabéns! Você acertou o número escolhido!\n')
            print('Você fez {} pontos'.format(pontos))
            break

        if (rodada == numero_tentativas):
            print('Você perdeu. O número secreto era {}.'.format(numero_secreto))
    print('Fim do jogo!')

if __name__ == '__main__':
    jogar()

# Constantes
# rodada = 1
# numero_tentativas = 0 #5
# limite_menor = 1
# limite_maior = 100
# numero_secreto = 32 #randint(limite_menor,limite_maior)
# print(numero_secreto)
# contador = 0
# nivel = 0
# pontos = 1000
# pontos_perdidos = 0
#
# # Nível de dificuldade
# # print(' Escolha o nível de dificuldade: \n(1) Fácil (2) Médio (3) Difícil')
# # nivel = int(input('Digite o número: '))
# while contador < 1:
#     print('\nEscolha o nível de dificuldade: \n(1) Fácil (2) Médio (3) Difícil')
#     try:
#         nivel = int(input('Digite o número: '))
#     except ValueError:
#         print('Por favor, digite um número válido. ')
#     #nivel = int(input('Digite o número: '))
#     if nivel == 1:
#         numero_tentativas = 10
#         break
#     elif nivel == 2:
#         numero_tentativas = 5
#         break
#     elif nivel == 3:
#         numero_tentativas = 3
#         #contador +=1
#         break
#     else:
#         print('Por favor, digite um número válido. ')
#         continue
#
# # if nivel == 1:
# #     numero_tentativas = 10
# # elif nivel == 2:
# #     numero_tentativas = 5
# # elif nivel == 3:
# #     numero_tentativas = 3
# # else:
# #     print('Por favor, digite um número válido. ')
#
# # Loop
# for rodada in range(1, numero_tentativas+1):
#     print('{}ª tentativa de {}'.format(rodada,numero_tentativas))
#     print(pontos_perdidos)
#     print(type(pontos_perdidos))
#     print(pontos)
#     try:
#         palpite = int(input('Digite um número entre {} a {}: '.format(limite_menor,limite_maior)))
#     except ValueError:
#         print("Ops! Você não digitou um número válido. Tente novamente!\n")
#         continue
#
#     # Variáveis
#     maior = palpite > numero_secreto
#     menor = palpite < numero_secreto
#
#     # Condição errada
#     if (palpite < limite_menor or palpite > limite_maior):
#         print('O número escolhido não está entre {} e {}'.format(limite_menor,limite_maior) + '.\n')
#         continue
#
#
#
#     # Condição correta
#     if maior:
#         print('O número escolhido é maior que o número secreto!\n')
#         pontos_perdidos = abs(palpite - numero_secreto)//3
#         pontos = pontos - pontos_perdidos
#     elif menor:
#         print('O número escolhido é menor que o número secreto!\n')
#         pontos_perdidos = abs(palpite - numero_secreto)//3
#         pontos = pontos - pontos_perdidos
#     else:
#         print('Parabéns! Você acertou o número escolhido!\n')
#         print('Você fez {} pontos'.format(pontos))
#         break
#
# print('Fim do jogo!')
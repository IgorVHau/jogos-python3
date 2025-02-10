# print('*** Bem vindo ao jogo da letra ***')

def jogar():
    print('*** Bem vindo ao jogo da letra ***')
    # Constantes/Variáveis
    palavra_secreta = "python".upper()
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcado = False
    acerto = False
    erro = 0

    # Loop
    while(not enforcado and not acerto):
        print(letras_acertadas)
        palpite = input('Escolha uma letra: ').upper().strip()

        if(palpite in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(palpite == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erro += 1

        #Condição para o enforcado = True
        enforcado = erro >= 6

        #Condição para o acerto = True
        acerto = "_" not in letras_acertadas

        #Mensagens de jogo encerrado
        if(enforcado):
            print('Você perdeu!')
        if(acerto):
            print('Você ganhou!')

    print('Fim do jogo!')

if __name__ == '__main__':
    jogar()




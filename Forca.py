# print('*** Bem vindo ao jogo da letra ***')

def jogar():
    print('*** Bem vindo ao jogo da letra ***')
    # Constantes/Variáveis
    palavra_secreta = "python".upper()
    #letras_acertadas = ["_","_","_","_","_","_"]
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcado = False
    acerto = False
    erro = 0
    tentativa = 6

    # Loop
    while(not enforcado and not acerto):
        print(letras_acertadas)
        if tentativa - erro == 1:
            print('Você só tem mais {} tentativa.'.format(tentativa - erro))
        else:
            print('Você tem {} tentativas.'.format(tentativa - erro))
        #print('Número de tentativa(s): {}'.format(tentativa - erro))
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
        enforcado = erro == tentativa

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




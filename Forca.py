# print('*** Bem vindo ao jogo da letra ***')

def jogar():
    print('*** Bem vindo ao jogo da letra ***')
    # Constantes
    palavra_secreta = "banana".upper()
    enforcado = False
    acerto = False

    # Loop
    while(not enforcado and not acerto):
        palpite = input('Escolha uma letra: ').upper().strip()
        print('Jogando...')

        index = 0
        for letra in palavra_secreta:
            if(palpite == letra):
                print('Encontrei a letra {1} na posição {0}.'.format(index,letra))
            index += 1

    print('Fim do jogo!')

if __name__ == '__main__':
    jogar()




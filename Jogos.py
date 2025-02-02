import Adivinhacao
import Forca

def jogar():
    try:
        print('Qual jogo você quer jogar?\n(1) Adivinhação (2) Forca (3) Sair')
        jogo = int(input('Digite um número: '))
        print('\n')

        if jogo == 1:
            Adivinhacao.jogar()
        elif jogo == 2:
            Forca.jogar()
        elif jogo == 3:
            print('Volte quando quiser.\n')
        else:
            print('Por favor, digite uma opção válida.\n')
            jogar()
    except ValueError:
        print('Você não digitou um número válido')


if __name__ == '__main__':
    jogar()
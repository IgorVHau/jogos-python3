import random

def jogar():
    apresentar_abertura()
    palavra_secreta = ler_palavra_secreta()
    letras_acertadas = iniciar_palavra_secreta(palavra_secreta)

    # Constantes/Variáveis
    enforcado = False
    acerto = False
    erro = 0
    tentativa = 6

    # Loop
    while(not enforcado and not acerto):
        palpite = apresentar_forca(letras_acertadas, tentativa, erro)

        if palpite in palavra_secreta:
            preencher_letra(palpite, palavra_secreta, letras_acertadas)
        else:
            erro += 1

        enforcado = erro == tentativa
        acerto = "_" not in letras_acertadas

        apresentar_resultado(palavra_secreta, enforcado, acerto)

    print('Fim do jogo!')

# Funções
def apresentar_abertura():
    print('*** Bem vindo ao jogo da forca ***')

def ler_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def iniciar_palavra_secreta(palavra):
    return ["_" for letra in palavra]

def apresentar_forca(letras, tentativa, erro):
    print(letras)
    if tentativa - erro == 1:
        print('Você só tem mais {} tentativa.'.format(tentativa - erro))
    else:
        print('Você tem {} tentativas.'.format(tentativa - erro))
    # print('Número de tentativa(s): {}'.format(tentativa - erro))
    palpite = input('Escolha uma letra: ').upper().strip()
    return palpite

def preencher_letra(palpite, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if palpite == letra:
            letras_acertadas[index] = letra
        index += 1

def apresentar_resultado(palavra_secreta, enforcado, acerto):
    if enforcado:
        print('Você perdeu! A palavra era {}.'.format(palavra_secreta))
    if acerto:
        print('Você ganhou!')

if __name__ == '__main__':
    jogar()




def computador_escolhe_jogada(n, m):
    # Estratégia: deixar múltiplos de (m+1)
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            return i
    return min(n, m)

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada < 1 or jogada > m or jogada > n:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_computador = False
    else:
        print("Computador começa!")
        vez_do_computador = True

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peça{'s' if jogada > 1 else ''}.")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peça{'s' if jogada > 1 else ''}.")

        n -= jogada
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        elif n > 1:
            print(f"Agora restam {n} peças no tabuleiro.\n")

        vez_do_computador = not vez_do_computador

    if vez_do_computador:
        print("Fim do jogo! Você ganhou!")
    else:
        print("Fim do jogo! O computador ganhou!")

def campeonato():
    print("Você escolheu um campeonato!")
    placar_usuario = 0
    placar_computador = 0

    for rodada in range(1, 4):
        print(f"**** Rodada {rodada} ****")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

        if n % (m + 1) == 0:
            print("Você começa!")
            vez_do_computador = False
        else:
            print("Computador começa!")
            vez_do_computador = True

        while n > 0:
            if vez_do_computador:
                jogada = computador_escolhe_jogada(n, m)
                print(f"O computador tirou {jogada} peça{'s' if jogada > 1 else ''}.")
            else:
                jogada = usuario_escolhe_jogada(n, m)
                print(f"Você tirou {jogada} peça{'s' if jogada > 1 else ''}.")

            n -= jogada
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif n > 1:
                print(f"Agora restam {n} peças no tabuleiro.\n")

            vez_do_computador = not vez_do_computador

        if vez_do_computador:
            print("Fim do jogo! Você ganhou!")
            placar_usuario += 1
        else:
            print("Fim do jogo! O computador ganhou!")
            placar_computador += 1

    print("**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha = int(input())

    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        campeonato()

main()

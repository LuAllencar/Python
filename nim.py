
def campeonato():
    print("Você escolheu um campeonato!")
    rodadas = 3
    vitorias_usuario = 0
    vitorias_computador = 0
    
    for i in range(rodadas):
        print(f"\n**** Rodada {i + 1} ****")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        
        while n > 0 and:
            print(f"\nRestam {n} peças no tabuleiro.")
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            if n == 0:
                print("Você ganhou!")
                vitorias_usuario += 1
                break
            
            print(f"\nRestam {n} peças no tabuleiro.")
            jogada_computador = computador_escolhe_jogada(n, m)
            n -= jogada_computador
            if n == 0:
                print("O computador ganhou!")
                vitorias_computador += 1
                break
    
    print("\n**** Final do campeonato! ****")
    print(f"Placar: Você {vitorias_usuario} X {vitorias_computador} Computador")

def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0:
        return ("Você começa!")
    else:
        return ("Computador começa!")
    
def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            return jogada
        else:
            print("Oops! Jogada inválida! Tente de novo.")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    while n > 0:
        print(f"\nRestam {n} peças no tabuleiro.")
        jogada_usuario = usuario_escolhe_jogada(n, m)
        n -= jogada_usuario
        if n == 0:
            print("Você ganhou!")
            break
        
        print(f"\nRestam {n} peças no tabuleiro.")
        jogada_computador = computador_escolhe_jogada(n, m)
        n -= jogada_computador
        if n == 0:
            print("O computador ganhou!")
            break

print("\nBem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

if input() == "1":
    print("Você escolheu uma partida isolada!")
    partida()
elif input() == "2":
    print("Você escolheu um campeonato!")

    
    while n > 0:
        print(f"\nRestam {n} peças no tabuleiro.")
        jogada_usuario = usuario_escolhe_jogada(n, m)
        n -= jogada_usuario
        if n == 0:
            print("Você ganhou!")
            break
        
        print(f"\nRestam {n} peças no tabuleiro.")
        jogada_computador = computador_escolhe_jogada(n, m)
        n -= jogada_computador
        if n == 0:
            print("O computador ganhou!")
            break

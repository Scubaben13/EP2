def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio not in frota:
        frota[nome_navio] = [posicoes]
    else:
        frota[nome_navio].append(posicoes)
    
    return frota

          

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for navio in frota:
        for posicoes in frota[navio]:
            for pos in posicoes:
                linha = pos[0]
                coluna = pos[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro


def afundados(frota, tabuleiro):
    contador = 0
    for lista_navios in frota.values():
        for posicoes in lista_navios:
            if all(tabuleiro[linha][coluna] == 'X' for linha, coluna in posicoes):
                contador += 1
    return contador



def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for pos in posicoes:
        if pos[0] > 9 or pos[1] > 9:
            return False

    todas_posicoes = []
    for lista_navios in frota.values():
        for posicoes_navio in lista_navios:
            for p in posicoes_navio:
                todas_posicoes.append(p)

    for pos in posicoes:
        if pos in todas_posicoes:
            return False

    return True




frota = {"porta-aviões": [], "navio-tanque": [], "contratorpedeiro": [], "submarino": []}

navios = [("porta-aviões", 4, 1), ("navio-tanque", 3, 2), ("contratorpedeiro", 2, 3), ("submarino", 1, 4)]

for nome, tamanho, quantidade in navios:
    for _ in range(quantidade):
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        pos_valida = False
        while not pos_valida:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome == "submarino":
                orientacao = "vertical"
            else:
                orient_num = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orient_num == 1 else "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                pos_valida = True
            else:
                print("Esta posição não está válida!")

print(frota)














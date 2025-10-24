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










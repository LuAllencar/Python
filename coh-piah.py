import re
texto = ""
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("\nEntre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        if texto == "":
            break
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    soma = 0
    for i in range(6):
        soma += abs(as_a[i] - as_b[i])
    return soma / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # tamanho médio da palavra

    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []

    for sentenca in sentencas:
            x = separa_frases(sentenca)
            frases.extend(x)
            for frase in x:
                y = separa_palavras(frase)
                palavras.extend(y)

    soma_palavras = 0
    for palavra in palavras:
        soma_palavras += len(palavra)
    tamanho_medio_palavra = soma_palavras / len(palavras)

    # type-token
    type_token = n_palavras_diferentes(palavras) / len(palavras)

    # hapax legomana
    hapax_legomana = n_palavras_unicas(palavras) / len(palavras)

    # tamanho médio da sentença
    soma_sentencas = 0
    for sentenca in sentencas:
        soma_sentencas += len(sentenca)
    tamanho_medio_sentenca = soma_sentencas / len(sentencas)

    # complexididade da sentença
    complexidade_sentenca = len(frases) / len(sentencas)

    # tamanho médio da frase
    soma_frases = 0
    for frase in frases:
        soma_frases += len(frase)
    tamanho_medio_frase = soma_frases / len(frases)
    return [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    

    aux_similaridade = float('inf')
    texto_infec = 0

    for i in range(len(textos)):
        ass = calcula_assinatura(textos[i])
        similaridade = compara_assinatura(ass, ass_cp)

        if similaridade < aux_similaridade:
            aux_similaridade = similaridade
            texto_infec = i + 1

    return texto_infec

assinatura_infectado = le_assinatura()
textos = le_textos()
numero_texto_infectado = avalia_textos(textos, assinatura_infectado)

print("\nO autor do texto", numero_texto_infectado, "está infectado com COH-PIAH.")

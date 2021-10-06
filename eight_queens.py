enablePrints = 0
from ctypes import sizeof
import random

def main():
    run_ga(5000, 30, 30, 0.01, True)

def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    conflitos = 0

    #checa conflitos na mesma linha
    for atual in individual:
        for comparacaoAtual in individual:
            if atual == comparacaoAtual:
                conflitos = conflitos+1
            else: 
                pass
    conflitos = conflitos - 8 #-8 conflitos com elas mesmas

    #aqui procura conflitos nas diagonais
    indexAtual = 1
    indexComparaAtual = 1
    for atual in individual:
        for comparacaoAtual in individual:
            if indexComparaAtual != indexAtual:
                posConflitante = abs(indexAtual - indexComparaAtual)
                if (comparacaoAtual == atual + posConflitante) or (comparacaoAtual == atual - posConflitante):
                    conflitos = conflitos + 1
                else:
                    pass
            else:
                pass 
            indexComparaAtual = indexComparaAtual + 1   
        indexComparaAtual = 1
        indexAtual = indexAtual + 1
    
    conflitos = int(conflitos/2) #pois está contando o numero de ataques, 1 ataca 2 e vice versa
    
    if enablePrints: print(conflitos)     #debug

    return conflitos

def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    conflitosMelhor = 30 #o maior numero de conflitos possível é 28
    indexMelhor = 0
    indexAtual = 0
    for individual in participants:
        conflitos = evaluate(individual)
        if conflitos < conflitosMelhor:
            indexMelhor = indexAtual
        indexAtual = indexAtual + 1

    if enablePrints: print(participants[indexMelhor])

    return participants[indexMelhor]

def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    parent1temp = parent1[:]

    filho1 = parent1[:]
    filho2 = parent2[:]

    indextemp = 7
    while indextemp >= index:
        filho1[indextemp] = parent2[indextemp]
        indextemp = indextemp - 1

    indextemp = 7
    while indextemp >= index:
        filho2[indextemp] = parent1temp[indextemp]
        indextemp = indextemp - 1
    
    if enablePrints: print(filho1, filho2)

    filhos = [filho1, filho2]
    return filhos

def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    mutation = round(random.uniform(0.0, 1.0), 3)
    if mutation < m:
        mutationPosition = random.randint(0,7)
        mutationValue = random.randint(0,7)
        individual[mutationPosition] = mutationValue

    if enablePrints: print(individual)

    return individual

def generateParent():
    parent = [0,0,0,0,0,0,0,0]

    index = 0
    while index < 8:
        queen = random.randint(1,8)
        parent[index] = queen
        index = index + 1

    if enablePrints: print(parent)

    return parent

def top(participants, n, k):
    selectParticipants = participants[:]
    participantes = []
    melhores = []

    indexParticipants = 0
    while indexParticipants < k:
        participantNumber = random.randint(0, len(selectParticipants)-1)
        participantes.append(selectParticipants[participantNumber])
        selectParticipants.pop(participantNumber)
        indexParticipants = indexParticipants + 1
        
    index = 0
    while index < n:
        melhor = tournament(participantes)
        participantes.remove(melhor)
        melhores.append(melhor)
        index = index + 1

    return melhores

def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    p = []
    
    #gera a lista de pais baseada no numero n de indivíduos
    i = 0
    while i < n:
        p.append(generateParent())
        i = i + 1

    geracaoAtual = 0
    while geracaoAtual < g:
        if e:
            pFilhos = []
            pFilhos.append(tournament(p))
        else:    
            pFilhos = []
        while len(pFilhos) < n:
            pFilhosTemp = []
            pFilhosTemp.clear()
            melhores = top(p, 2, k)
            pFilhosTemp = crossover(melhores[0], melhores[1], random.randint(0,7))
            mutate(pFilhosTemp[0],m)
            mutate(pFilhosTemp[1],m)
            pFilhos.extend(pFilhosTemp)

        p = pFilhos[:]
        geracaoAtual = geracaoAtual + 1

    melhorDosMelhores = tournament(p)

    print(melhorDosMelhores, "Ataques: ", evaluate(melhorDosMelhores))
    

if __name__ == "__main__":
    main()
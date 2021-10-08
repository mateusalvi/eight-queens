import numpy as np


def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """

    mse=0
    sum=0
    quad=0
    i=0

    while(i < len(data)):
        h = theta_0 + (theta_1*data[i][0]) 
        aux = h - data[i][1]
        quad = aux**2
        sum = sum + quad
        i = i + 1

    mse = sum/len(data)

    return mse

def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """

    i=0
    f1=0
    f2=0
    sumf1=0
    sumf2=0
    df1=0
    df2=0
    up_theta0=0
    up_theta1=0
    thetas = []

    while(i < len(data)):
        h = theta_0 + (theta_1*data[i][0]) 
        f1 = h - data[i][1]
        f2 = f1*data[i][0]
        sumf1 = sumf1 + f1
        sumf2 = sumf2 + f2
        i = i + 1
    
    df1 = (2*sumf1)/len(data)
    df2 = (2*sumf2)/len(data)

    up_theta0 = theta_0 - (alpha*df1)
    up_theta1 = theta_1 - (alpha*df2)

    thetas.append(up_theta0)
    thetas.append(up_theta1)

    return thetas

def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    theta0 = []
    theta1 = []
    aux = []
    thetas01 = []
    element = 0

    aux.append(step_gradient(theta_0, theta_1, data, alpha))
    element = aux.pop()
    theta1.append(element[1])
    theta0.append(element[0])

    i=1
    while (i < num_iterations):
        aux.append(step_gradient(element[0], element[1], data, alpha))
        element = aux.pop()
        theta1.append(element[1])
        theta0.append(element[0])
        i = i + 1


    thetas01.append(theta0)
    thetas01.append(theta1)

    print(thetas01)
    return thetas01
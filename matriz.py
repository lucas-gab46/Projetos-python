# Autor: Lucas Gabriel De Camargo Santos (832792)
# Data de Criação: 14/08/24
# Data de Alteração: 14/08/24
# Objetivo: Multiplicar Matriz A e B e aparecer a Multiplicação na Tela Por Linha

MAX_COLUNAS = 3
MAX_LINHAS = 3

def ler_matriz(nome_matriz):
    matriz = []
    print(f"Digite os valores da Matriz {nome_matriz}:")
    for i in range(MAX_LINHAS):
        linha = []
        for j in range(MAX_COLUNAS):
            valor = int(input(f"Digite o valor da linha {i + 1}, coluna {j + 1}: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def e_matriz_identidade(matriz):
    for i in range(MAX_LINHAS):
        for j in range(MAX_COLUNAS):
            if i == j and matriz[i][j] != 1:
                return False
            if i != j and matriz[i][j] != 0:
                return False
    return True

def multiplicar_matrizes(matrizA, matrizB):
    resultado = [[0] * MAX_COLUNAS for _ in range(MAX_LINHAS)]
    for i in range(MAX_LINHAS):
        for j in range(MAX_COLUNAS):
            for k in range(MAX_COLUNAS):
                resultado[i][j] += matrizA[i][k] * matrizB[k][j]
    return resultado

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

def main():
    matrizA = ler_matriz("A")
    matrizB = ler_matriz("B")


    resultado = multiplicar_matrizes(matrizA, matrizB)
    print("A multiplicação das matrizes A e B resulta em:")
    imprimir_matriz(resultado)

if __name__ == "__main__":
    main()

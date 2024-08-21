# Autor: Lucas Gabriel De Camargo Santos (832792)
# Data de Criação: 14/08/24
# Data de Alteração: 14/08/24
# Objetivo: Mostrar o Maior Valor Da Matriz e mostrar Resultado

def main():
    MAX_colunas = 3
    MAX_linhas = 3

    # Inicializando as matrizes
    matrizA = [[0] * MAX_colunas for _ in range(MAX_linhas)]
    matrizB = [[0] * MAX_colunas for _ in range(MAX_linhas)]

    print("Digite os valores da Matriz A:")
    for i in range(MAX_linhas):
        for j in range(MAX_colunas):
            matrizA[i][j] = int(input(f"Digite o valor da linha {i + 1}, coluna {j + 1}: "))

    print("Digite os valores da Matriz B:")
    for i in range(MAX_linhas):
        for j in range(MAX_colunas):
            matrizB[i][j] = int(input(f"Digite o valor da linha {i + 1}, coluna {j + 1}: "))

    # Encontrando o maior valor nas matrizes
    max_valor_a = max(max(row) for row in matrizA)
    max_valor_b = max(max(row) for row in matrizB)

    # Comparando os maiores valores e mostrando o resultado
    if max_valor_a > max_valor_b:
        print(f"O Maior Valor é da Matriz A: {max_valor_a}")
    elif max_valor_b > max_valor_a:
        print(f"O Maior Valor é da Matriz B: {max_valor_b}")
    else:
        print(f"Ambas as Matrizes têm o mesmo maior valor: {max_valor_a}")

if __name__ == "__main__":
    main()

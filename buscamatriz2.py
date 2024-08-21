
#Autor: Lucas Gabriel de Camargo Santos (832792)
#Data de Criação: 12/08/24
#Data de Alteração: 12/08/24
#Objetivo: Leia Dois Valores Inteiros de Matriz e deve fornecer um Valor de Busca






def main():
    max_linhas = 10
    max_colunas = 10

    # Leitura das dimensões da matriz
    linhas = int(input(f"Digite o número de linhas (máximo {max_linhas}): "))
    colunas = int(input(f"Digite o número de colunas (máximo {max_colunas}): "))

    if linhas > max_linhas or colunas > max_colunas or linhas <= 0 or colunas <= 0:
        print("Número de linhas ou colunas inválido.")
        return

    matriz = []

    # Leitura dos elementos da matriz
    print("Digite os elementos da matriz:")
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"Elemento [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    # Leitura da chave de busca
    chave = int(input("Digite o valor a ser buscado: "))

    # Busca na matriz
    encontrado = False
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == chave:
                print(f"Valor {chave} encontrado na posição [{i}][{j}].")
                encontrado = True
                break
        if encontrado:
            break

    if not encontrado:
        print(f"Valor {chave} não encontrado na matriz.")

if __name__ == "__main__":
    main()

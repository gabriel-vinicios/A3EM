def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Valor deve ser ≥ {minimo}. Tente novamente.")
            elif maximo is not None and valor > maximo:
                print(f"Valor deve ser ≤ {maximo}. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def ler_matriz(n):
    A = [[0.0]*n for _ in range(n)]
    b = [0.0]*n
    print("\nInforme os coeficientes da matriz A e do termo independente b:")
    for i in range(n):
        for j in range(n):
            while True:
                try:
                    A[i][j] = float(input(f"A[{i+1},{j+1}] = "))
                    break
                except ValueError:
                    print("Número inválido. Tente novamente.")
        while True:
            try:
                b[i] = float(input(f"b[{i+1}] = "))
                break
            except ValueError:
                print("Número inválido. Tente novamente.")
    return A, b

def eliminacao_gauss(A, b):
    n = len(A)
    # Pivoteamento parcial e eliminação
    for k in range(n):
        # encontra o maior pivô na coluna k abaixo (e incluindo) a linha k
        max_row = max(range(k, n), key=lambda i: abs(A[i][k]))
        if abs(A[max_row][k]) < 1e-12:
            return None  # sistema singular ou mal condicionado
        # troca de linhas
        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k]
            b[k], b[max_row] = b[max_row], b[k]
        # elimina abaixo
        for i in range(k+1, n):
            fator = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= fator * A[k][j]
            b[i] -= fator * b[k]
    # retro-substituição
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        soma = sum(A[i][j]*x[j] for j in range(i+1, n))
        x[i] = (b[i] - soma) / A[i][i]
    return x

def imprimir_solucao(x):
    print("\nSolução encontrada:")
    for i, xi in enumerate(x, start=1):
        print(f"x[{i}] = {xi:.6f}")

def main():
    print("=== CALCULADORA DE SISTEMAS LINEARES (até 10×10) ===")
    while True:
        n = ler_inteiro("Dimensão do sistema n (1–10): ", 1, 10)
        A, b = ler_matriz(n)
        # cópias para não alterar original em caso de nova tentativa
        import copy
        A_copy = copy.deepcopy(A)
        b_copy = copy.deepcopy(b)
        sol = eliminacao_gauss(A_copy, b_copy)
        if sol is None:
            print("\nO sistema é singular ou mal condicionado. Não há solução única.")
        else:
            imprimir_solucao(sol)
        cont = input("\nDeseja resolver outro sistema? (s/N): ").strip().lower()
        if cont != 's':
            print("Encerrando a calculadora. Até logo!")
            break

if __name__ == "__main__":
    main()
"""
Calculadora de Sistemas Lineares
--------------------------------

Este programa implementa uma interface gráfica para resolução de sistemas lineares de equações, permitindo ao usuário escolher entre os métodos de Gauss, Gauss-Jordan, Regra de Cramer e Montante.

- Desenvolvido em Python com Tkinter.
- Aceita apenas matrizes quadradas (n x n).
- Permite entrada manual dos coeficientes e termos independentes.
- Exibe a solução ou mensagens de erro apropriadas.
"""

import tkinter as tk
from tkinter import messagebox

# ----------------------
# Métodos Numéricos
# ----------------------
def gauss_jordan(A, b):
    """
    Resolve o sistema linear Ax = b pelo método de Gauss-Jordan.
    Transforma a matriz aumentada em identidade e retorna o vetor solução x.
    Retorna None se o sistema for singular ou não quadrado.
    """
    n = len(A)
    m = len(A[0])
    if n != m:
        return None
    # Monta matriz aumentada
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        # Pivoteamento
        max_row = max(range(i, n), key=lambda r: abs(M[r][i]))
        if abs(M[max_row][i]) < 1e-12:
            return None
        if max_row != i:
            M[i], M[max_row] = M[max_row], M[i]
        # Normaliza linha
        piv = M[i][i]
        M[i] = [v / piv for v in M[i]]
        # Zera as outras linhas
        for j in range(n):
            if j != i:
                fator = M[j][i]
                M[j] = [M[j][k] - fator * M[i][k] for k in range(n+1)]
    return [M[i][-1] for i in range(n)]

# ----------------------
# Interface Gráfica
# ----------------------
class SistemaLinearApp:
    """
    Classe principal da interface gráfica para resolução de sistemas lineares.
    Permite ao usuário escolher a ordem da matriz e inserir os coeficientes.
    """
    def __init__(self, root):
        # Inicializa a janela principal e variáveis de controle
        self.root = root
        self.root.title("Calculadora de Sistemas Lineares")
        self.n = tk.IntVar(value=2)  # ordem da matriz quadrada
        self.entries_A = []
        self.entries_b = []
        self.setup_dimensao()

    def setup_dimensao(self):
        """
        Exibe a tela para seleção da ordem da matriz quadrada.
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Ordem da matriz quadrada (n x n):\n(n = número de linhas = número de colunas)").pack()
        frame_dim = tk.Frame(self.root)
        frame_dim.pack()
        tk.Label(frame_dim, text="Ordem (n):").grid(row=0, column=0)
        tk.Spinbox(frame_dim, from_=1, to=10, textvariable=self.n, width=5).grid(row=0, column=1)
        tk.Button(self.root, text="Confirmar", command=self.setup_matriz).pack(pady=10)

    def setup_matriz(self):
        """
        Exibe a tela para entrada dos coeficientes da matriz A e do vetor b.
        """
        n = self.n.get()
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"Insira os coeficientes da matriz A ({n} linhas x {n} colunas) e vetor b ({n} linhas):").pack()
        frame = tk.Frame(self.root)
        frame.pack()
        self.entries_A = []
        self.entries_b = []
        for i in range(n):
            row_entries = []
            for j in range(n):
                e = tk.Entry(frame, width=5)
                e.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(e)
            self.entries_A.append(row_entries)
            e_b = tk.Entry(frame, width=5, bg="#e0f7fa")
            e_b.grid(row=i, column=n, padx=5)
            self.entries_b.append(e_b)
        tk.Label(self.root, text="Cada linha representa uma equação e cada coluna representa uma incógnita.").pack(pady=(5,0))
        tk.Button(self.root, text="Calcular", command=self.calcular).pack(pady=10)
        tk.Button(self.root, text="Alterar ordem", command=self.setup_dimensao).pack()

    def calcular(self):
        """
        Lê os valores inseridos, executa o método de Eliminação de Gauss-Jordan e exibe o resultado ou mensagem de erro.
        """
        n = self.n.get()
        try:
            A = [[float(self.entries_A[i][j].get()) for j in range(n)] for i in range(n)]
            b = [float(self.entries_b[i].get()) for i in range(n)]
        except ValueError:
            messagebox.showerror("Erro", "Preencha todos os campos com números válidos.")
            return
        A_copia = [row[:] for row in A]
        b_copia = b[:]
        sol = gauss_jordan(A_copia, b_copia)
        if sol is None:
            messagebox.showinfo("Resultado", "O sistema é singular, mal condicionado ou não possui solução única.")
        else:
            resultado = "\n".join([f"x[{i+1}] = {xi:.6f}" for i, xi in enumerate(sol)])
            messagebox.showinfo("Solução encontrada", resultado)

if __name__ == "__main__":
    # Inicializa e executa a aplicação Tkinter
    root = tk.Tk()
    app = SistemaLinearApp(root)
    root.mainloop()
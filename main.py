import tkinter as tk
from tkinter import messagebox

def eliminacao_gauss(A, b):
    n = len(A)
    for k in range(n):
        max_row = max(range(k, n), key=lambda i: abs(A[i][k]))
        if abs(A[max_row][k]) < 1e-12:
            return None
        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k]
            b[k], b[max_row] = b[max_row], b[k]
        for i in range(k+1, n):
            fator = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= fator * A[k][j]
            b[i] -= fator * b[k]
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        soma = sum(A[i][j]*x[j] for j in range(i+1, n))
        x[i] = (b[i] - soma) / A[i][i]
    return x

def gauss_jordan(A, b):
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

def determinante(M):
    # Calcula determinante por eliminação de Gauss
    n = len(M)
    A = [row[:] for row in M]
    det = 1
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if abs(A[max_row][i]) < 1e-12:
            return 0
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            det *= -1
        det *= A[i][i]
        for j in range(i+1, n):
            fator = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]
    return det

def cramer(A, b):
    n = len(A)
    if n != len(A[0]):
        return None
    det_A = determinante(A)
    if abs(det_A) < 1e-12:
        return None
    x = []
    for i in range(n):
        Ai = [row[:] for row in A]
        for j in range(n):
            Ai[j][i] = b[j]
        det_Ai = determinante(Ai)
        x.append(det_Ai / det_A)
    return x

def montante(A, b):
    n = len(A)
    if n != len(A[0]):
        return None
    # Monta matriz aumentada
    M = [A[i][:] + [b[i]] for i in range(n)]
    p = 1
    for k in range(n):
        piv = M[k][k]
        if abs(piv) < 1e-12:
            return None
        for i in range(n):
            if i != k:
                for j in range(k+1, n+1):
                    M[i][j] = (M[k][k]*M[i][j] - M[i][k]*M[k][j]) / p
                M[i][k] = 0
        p = piv
    return [M[i][n]/M[i][i] for i in range(n)]

class SistemaLinearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Sistemas Lineares")
        self.n = tk.IntVar(value=2)  # ordem da matriz quadrada
        self.entries_A = []
        self.entries_b = []
        self.metodo = tk.StringVar(value="Gauss")
        self.setup_dimensao()

    def setup_dimensao(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Ordem da matriz quadrada (n x n):\n(n = número de linhas = número de colunas)").pack()
        frame_dim = tk.Frame(self.root)
        frame_dim.pack()
        tk.Label(frame_dim, text="Ordem (n):").grid(row=0, column=0)
        tk.Spinbox(frame_dim, from_=1, to=10, textvariable=self.n, width=5).grid(row=0, column=1)
        tk.Label(self.root, text="Método de resolução:").pack(pady=(10,0))
        frame_met = tk.Frame(self.root)
        frame_met.pack()
        metodos = ["Gauss", "Gauss-Jordan", "Cramer", "Montante"]
        for i, nome in enumerate(metodos):
            tk.Radiobutton(frame_met, text=nome, variable=self.metodo, value=nome).grid(row=0, column=i)
        tk.Button(self.root, text="Confirmar", command=self.setup_matriz).pack(pady=10)

    def setup_matriz(self):
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
        n = self.n.get()
        try:
            A = [[float(self.entries_A[i][j].get()) for j in range(n)] for i in range(n)]
            b = [float(self.entries_b[i].get()) for i in range(n)]
        except ValueError:
            messagebox.showerror("Erro", "Preencha todos os campos com números válidos.")
            return
        metodo = self.metodo.get()
        if metodo == "Gauss":
            A_copia = [row[:] for row in A]
            b_copia = b[:]
            sol = eliminacao_gauss(A_copia, b_copia)
        elif metodo == "Gauss-Jordan":
            A_copia = [row[:] for row in A]
            b_copia = b[:]
            sol = gauss_jordan(A_copia, b_copia)
        elif metodo == "Cramer":
            sol = cramer(A, b)
        elif metodo == "Montante":
            sol = montante(A, b)
        else:
            messagebox.showerror("Erro", "Método não implementado.")
            return
        if sol is None:
            messagebox.showinfo("Resultado", "O sistema é singular, mal condicionado ou não possui solução única.")
        else:
            resultado = "\n".join([f"x[{i+1}] = {xi:.6f}" for i, xi in enumerate(sol)])
            messagebox.showinfo("Solução encontrada", resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaLinearApp(root)
    root.mainloop()
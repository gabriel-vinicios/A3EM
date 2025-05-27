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

class SistemaLinearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Sistemas Lineares")
        self.m = tk.IntVar(value=2)  # linhas
        self.n = tk.IntVar(value=2)  # colunas
        self.entries_A = []
        self.entries_b = []
        self.setup_dimensao()

    def setup_dimensao(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Dimensão da matriz A:").pack()
        frame_dim = tk.Frame(self.root)
        frame_dim.pack()
        tk.Label(frame_dim, text="Linhas (m):").grid(row=0, column=0)
        tk.Spinbox(frame_dim, from_=1, to=10, textvariable=self.m, width=5).grid(row=0, column=1)
        tk.Label(frame_dim, text="Colunas (n):").grid(row=0, column=2)
        tk.Spinbox(frame_dim, from_=1, to=10, textvariable=self.n, width=5).grid(row=0, column=3)
        tk.Button(self.root, text="Confirmar", command=self.setup_matriz).pack(pady=10)

    def setup_matriz(self):
        m = self.m.get()
        n = self.n.get()
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"Insira os coeficientes da matriz A ({m}x{n}) e vetor b ({m}):").pack()
        frame = tk.Frame(self.root)
        frame.pack()
        self.entries_A = []
        self.entries_b = []
        for i in range(m):
            row_entries = []
            for j in range(n):
                e = tk.Entry(frame, width=5)
                e.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(e)
            self.entries_A.append(row_entries)
            e_b = tk.Entry(frame, width=5, bg="#e0f7fa")
            e_b.grid(row=i, column=n, padx=5)
            self.entries_b.append(e_b)
        tk.Button(self.root, text="Calcular", command=self.calcular).pack(pady=10)
        tk.Button(self.root, text="Alterar dimensão", command=self.setup_dimensao).pack()

    def calcular(self):
        m = self.m.get()
        n = self.n.get()
        try:
            A = [[float(self.entries_A[i][j].get()) for j in range(n)] for i in range(m)]
            b = [float(self.entries_b[i].get()) for i in range(m)]
        except ValueError:
            messagebox.showerror("Erro", "Preencha todos os campos com números válidos.")
            return
        if m != n:
            messagebox.showerror("Erro", "O método de eliminação de Gauss só resolve sistemas quadrados (m = n).")
            return
        # Cópia manual das listas
        A_copia = [row[:] for row in A]
        b_copia = b[:]
        sol = eliminacao_gauss(A_copia, b_copia)
        if sol is None:
            messagebox.showinfo("Resultado", "O sistema é singular ou mal condicionado.\nNão há solução única.")
        else:
            resultado = "\n".join([f"x[{i+1}] = {xi:.6f}" for i, xi in enumerate(sol)])
            messagebox.showinfo("Solução encontrada", resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaLinearApp(root)
    root.mainloop()
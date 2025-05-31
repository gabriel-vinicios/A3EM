# Calculadora de Sistemas Lineares

Este software é uma calculadora gráfica para resolução de sistemas lineares de equações, desenvolvida em Python com a biblioteca Tkinter. Ele permite ao usuário inserir uma matriz quadrada de coeficientes e um vetor de termos independentes, e resolve o sistema utilizando diferentes métodos numéricos clássicos.

## Funcionalidades
- Interface gráfica intuitiva para entrada dos coeficientes da matriz A (n x n) e do vetor b (n x 1).
- Seleção do método de resolução entre:
  - Eliminação de Gauss
  - Gauss-Jordan
  - Regra de Cramer
  - Método de Montante
- Exibição clara dos resultados ou mensagens de erro caso o sistema não tenha solução única.
- Permite alterar facilmente a ordem da matriz (número de linhas e colunas).

## Como usar
1. Execute o arquivo `main.py`.
2. Escolha a ordem da matriz quadrada (n x n) usando o seletor.
3. Escolha o método de resolução desejado.
4. Clique em "Confirmar" para acessar a tela de entrada dos coeficientes.
5. Preencha os campos da matriz A (coeficientes das incógnitas) e do vetor b (termos independentes).
   - Cada linha representa uma equação.
   - Cada coluna representa uma incógnita.
6. Clique em "Calcular" para obter a solução.
7. O resultado será exibido em uma janela pop-up.

## Métodos implementados
- **Eliminação de Gauss:** Método clássico de escalonamento da matriz para obtenção da solução por substituição retroativa.
- **Gauss-Jordan:** Variante do método de Gauss que transforma a matriz em forma reduzida, obtendo a solução diretamente.
- **Regra de Cramer:** Utiliza determinantes para encontrar a solução, aplicável apenas a sistemas quadrados com determinante diferente de zero.
- **Método de Montante:** Algoritmo alternativo para resolução de sistemas lineares baseado em operações com determinantes.

## Fórmulas Matemáticas dos Métodos

### Eliminação de Gauss
O método consiste em transformar o sistema Ax = b em uma matriz triangular superior, usando operações elementares nas linhas:

- Para cada linha i > k:
$$
  \\[ a_{ij} = a_{ij} - \frac{a_{ik}}{a_{kk}} a_{kj} \quad \text{para}\ j = k, ..., n \\\\
  b_i = b_i - \frac{a_{ik}}{a_{kk}} b_k \\\\
\\]
$$
Após a matriz estar triangular, resolve-se por substituição retroativa:

\\[
  x_i = \frac{1}{a_{ii}} \left( b_i - \sum_{j=i+1}^n a_{ij} x_j \right)
\\]

### Gauss-Jordan
O método transforma a matriz aumentada [A|b] em uma matriz identidade:

- Para cada linha i:
  - Divide a linha i pelo pivô a_{ii} para tornar o pivô igual a 1.
  - Zera todos os outros elementos da coluna i:

\\[
  a_{kj} = a_{kj} - a_{ki} \cdot a_{ij} \quad \text{para}\ k \neq i
\\]

Ao final, a solução é:
\\[
  x_i = b_i
\\]

### Regra de Cramer
Para um sistema Ax = b, a solução é dada por:

\\[
  x_i = \frac{\det(A_i)}{\det(A)}
\\]

Onde A_i é a matriz A com a i-ésima coluna substituída pelo vetor b.

### Método de Montante
O método de Montante (Bareiss) é uma generalização do método de Gauss, mas preservando inteiros:

- Para cada etapa k:
  \\[ a_{ij}^{(k+1)} = \frac{a_{kk}^{(k)} a_{ij}^{(k)} - a_{ik}^{(k)} a_{kj}^{(k)}}{p} \quad \text{para}\ i \neq k, j \neq k \\\\
  p = a_{k-1,k-1}^{(k-1)} \ (p=1\ \text{na primeira etapa})
\\]

Ao final, a solução é obtida por:
\\[
  x_i = \frac{a_{i,n+1}}{a_{ii}}
\\]

## Cálculos em LaTeX dos Métodos

### Eliminação de Gauss
Dado o sistema:
\(
\begin{cases}
  a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
  a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
  \vdots \\
  a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n = b_n
\end{cases}
\)

A matriz aumentada é:
\(
\left[
\begin{array}{cccc|c}
  a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
  a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
  \vdots & \vdots & \ddots & \vdots & \vdots \\
  a_{n1} & a_{n2} & \cdots & a_{nn} & b_n
\end{array}
\right]
\)

Operação de eliminação:
\(
a_{ij}^{(k+1)} = a_{ij}^{(k)} - \frac{a_{ik}^{(k)}}{a_{kk}^{(k)}} a_{kj}^{(k)}
\)

Substituição retroativa:
\(
x_i = \frac{1}{a_{ii}} \left( b_i - \sum_{j=i+1}^n a_{ij} x_j \right)
\)

---

### Gauss-Jordan
Transforma a matriz aumentada em:
\(
\left[
\begin{array}{cccc|c}
  1 & 0 & \cdots & 0 & x_1 \\
  0 & 1 & \cdots & 0 & x_2 \\
  \vdots & \vdots & \ddots & \vdots & \vdots \\
  0 & 0 & \cdots & 1 & x_n
\end{array}
\right]
\)

Operação de pivoteamento e normalização:
\(
\text{Para cada linha } i:\quad \frac{L_i}{a_{ii}} \rightarrow L_i
\)

Zerando as outras linhas:
\(
L_k \leftarrow L_k - a_{ki} L_i \quad (k \neq i)
\)

---

### Regra de Cramer
Para o sistema \( Ax = b \):
\(
x_i = \frac{\det(A_i)}{\det(A)}
\)

Exemplo para 3x3:
\(
A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix},\quad
b = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}
\)

\(
A_1 = \begin{bmatrix} b_1 & a_{12} & a_{13} \\ b_2 & a_{22} & a_{23} \\ b_3 & a_{32} & a_{33} \end{bmatrix}
\)

\(
x_1 = \frac{\det(A_1)}{\det(A)}
\)

---

### Método de Montante
Para cada etapa k:
\(
a_{ij}^{(k+1)} = \frac{a_{kk}^{(k)} a_{ij}^{(k)} - a_{ik}^{(k)} a_{kj}^{(k)}}{p}
\)
Onde:
- \( p = a_{k-1,k-1}^{(k-1)} \) (\( p=1 \) na primeira etapa)

Ao final:
\(
x_i = \frac{a_{i,n+1}}{a_{ii}}
\)

---

## Estrutura do código
- `eliminacao_gauss(A, b)`: Função que implementa o método de Gauss.
- `gauss_jordan(A, b)`: Função que implementa o método de Gauss-Jordan.
- `determinante(M)`: Função auxiliar para cálculo de determinantes.
- `cramer(A, b)`: Função que implementa a Regra de Cramer.
- `montante(A, b)`: Função que implementa o método de Montante.
- `SistemaLinearApp`: Classe principal da interface gráfica, responsável por toda a interação com o usuário.

## Observações
- O programa aceita apenas sistemas quadrados (número de equações igual ao número de incógnitas).
- Todos os métodos implementados são clássicos e servem para fins didáticos e de estudo.
- Para sistemas singulares ou mal condicionados, o programa exibirá uma mensagem de erro.

## Requisitos
- Python 3.x
- Tkinter (normalmente já incluído na instalação padrão do Python)

## Autor
- Desenvolvido por Gabriel Vinicios, e Daniel Filho.

---

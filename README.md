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

# Calculadora de Sistemas Lineares

Este software é uma calculadora gráfica para resolução de sistemas lineares de equações, desenvolvida em Python com a biblioteca Tkinter. Ele permite ao usuário inserir uma matriz quadrada de coeficientes e um vetor de termos independentes, e resolve o sistema utilizando o método de Eliminação de Gauss-Jordan.

## Funcionalidades
- Interface gráfica intuitiva para entrada dos coeficientes da matriz A (n x n) e do vetor b (n x 1).
- Resolução do sistema linear exclusivamente pelo método de Eliminação de Gauss-Jordan.
- Exibição clara dos resultados ou mensagens de erro caso o sistema não tenha solução única.
- Permite alterar facilmente a ordem da matriz (número de linhas e colunas).

## Como usar
1. Execute o arquivo `main.py`.
2. Escolha a ordem da matriz quadrada (n x n) usando o seletor.
3. Clique em "Confirmar" para acessar a tela de entrada dos coeficientes.
4. Preencha os campos da matriz A (coeficientes das incógnitas) e do vetor b (termos independentes).
   - Cada linha representa uma equação.
   - Cada coluna representa uma incógnita.
5. Clique em "Calcular" para obter a solução.
6. O resultado será exibido em uma janela pop-up.

## Método implementado
- **Eliminação de Gauss-Jordan:** Transforma a matriz aumentada em forma reduzida por linhas, obtendo a solução diretamente.

## Estrutura do código
- `gauss_jordan(A, b)`: Função que implementa o método de Gauss-Jordan.
- `SistemaLinearApp`: Classe principal da interface gráfica, responsável por toda a interação com o usuário.

## Observações
- O programa aceita apenas sistemas quadrados (número de equações igual ao número de incógnitas).
- O método implementado é clássico e serve para fins didáticos e de estudo.
- Para sistemas singulares ou mal condicionados, o programa exibirá uma mensagem de erro.

## Requisitos
- Python 3.x
- Tkinter (normalmente já incluído na instalação padrão do Python)

## Autor
- Desenvolvido por Gabriel Vinicios e Daniel Filho.

---

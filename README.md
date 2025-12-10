# 🌵 O Pequeno Herói Verde

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
![Badge Python](http://img.shields.io/static/v1?label=LINGUAGEM&message=PYTHON&color=blue&style=for-the-badge)
![Badge Pygame Zero](http://img.shields.io/static/v1?label=LIBRARY&message=PYGAME%20ZERO&color=red&style=for-the-badge)

> **Nota:** Este projeto faz parte do meu portfólio de estudos em Análise e Desenvolvimento de Sistemas (ADS). O objetivo é aplicar conceitos de Lógica de Programação, Física de Jogos e Orientação a Objetos.

## 🎮 Sobre o Projeto

"O Pequeno Herói Verde" é um jogo de plataforma 2D clássico. O jogador controla um personagem que deve atravessar obstáculos, evitar inimigos e coletar itens para avançar de fase.

O foco do desenvolvimento não foi apenas criar o jogo, mas estruturar um código limpo e escalável, permitindo a fácil adição de novos níveis e mecânicas (como a "Fase 2" implementada recentemente).

### ✨ Funcionalidades

- **Sistema de Física:** Gravidade customizada, pulo e detecção de "chão".
- **Colisão Aprimorada:** Algoritmo para impedir que o personagem entre dentro de blocos sólidos (colisão horizontal e vertical separadas).
- **Máquina de Estados:** Controle de telas (Menu Inicial, Jogo, Vitória, Game Over).
- **Animação de Sprites:** O personagem muda de sprite dependendo da ação (parado, correndo, pulando) e direção.
- **Sistema de Fases:** Carregamento dinâmico de mapas baseados em matrizes de texto.

## 🛠️ Tecnologias e Conceitos Utilizados

Este projeto foi desenvolvido em **Python** utilizando a biblioteca **Pygame Zero**. Abaixo, alguns dos conceitos técnicos aplicados:

- **Orientação a Objetos (POO):** - Uso de **Classes** para criar o molde do `Heroi` e dos `Inimigos`.
  - Herança da classe `Actor` do Pygame Zero.
- **Estrutura de Dados:**
  - Uso de **Listas** e **Matrizes** (Listas de Strings) para desenhar o mapa do nível.
  - Uso de **Dicionários** para mapear caracteres do mapa para imagens de sprites.
- **Lógica de Jogo (Game Loop):**
  - Funções `update()` (lógica 60x por segundo) e `draw()` (renderização).
  - Tratamento de eventos de teclado e mouse.

## 📷 Screenshots

*(Aqui você deve colocar um print ou um GIF do jogo rodando. Veja a dica abaixo do código)*

## 🚀 Como rodar o projeto

### Pré-requisitos
Você precisa ter o [Python](https://www.python.org/) instalado em sua máquina.

### Passo a passo

1. Clone o repositório:
```bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)

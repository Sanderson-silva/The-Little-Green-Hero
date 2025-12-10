# 🌵 O Pequeno Herói Verde

![Status](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
![Python](http://img.shields.io/static/v1?label=LINGUAGEM&message=PYTHON&color=blue&style=for-the-badge)
![Pygame Zero](http://img.shields.io/static/v1?label=FRAMEWORK&message=PYGAME%20ZERO&color=red&style=for-the-badge)

> **Nota:** Este projeto foi desenvolvido como parte do meu portfólio acadêmico no curso de **Análise e Desenvolvimento de Sistemas (ADS)**. O objetivo principal é aplicar na prática conceitos de Lógica de Programação, Orientação a Objetos e Estrutura de Dados.

---

## 🎮 Sobre o Projeto

**O Pequeno Herói Verde** é um jogo de plataforma 2D desenvolvido em Python. O jogador controla um personagem que deve superar desafios de física, evitar inimigos com inteligência de movimento básica e alcançar o objetivo final.

O projeto não se limita apenas à jogabilidade, mas foca na **arquitetura do código**, demonstrando como gerenciar estados de jogo, colisões e renderização gráfica de forma organizada.

### ✨ Destaques Técnicos & Funcionalidades

* **Orientação a Objetos (POO):** Utilização de Classes para modularizar o `Heroi` e os `Inimigos`, aplicando conceitos de herança e encapsulamento.
* **Sistema de Física Customizado:** Implementação manual de gravidade, inércia e pulo, sem depender de motores físicos prontos.
* **Algoritmo de Colisão:** Lógica matemática para detecção de colisão retangular (Hitboxes) precisa entre o personagem e o cenário.
* **Gerenciamento de Fases:** Sistema escalável que lê mapas baseados em matrizes de texto (Arrays de Strings), permitindo criar novos níveis facilmente (Fase 1 e Fase 2 já implementadas).
* **Máquina de Estados:** Controle de fluxo do jogo alternando entre *Menu*, *Gameplay*, *Vitória* e *Game Over*.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Biblioteca Gráfica:** Pygame Zero (pgzero)
* **IDE/Editor:** VS Code / PyCharm

---

## 📂 Estrutura do Projeto

O código foi organizado visando legibilidade e manutenção:

```text
📁 O_Pequeno_Heroi
│
├── 📁 images/          # Sprites e assets gráficos
├── 📁 sounds/          # Efeitos sonoros e música de fundo
├── 📄 game.py          # Código fonte principal (Lógica do jogo)
└── 📄 README.md        # Documentação do projeto

"""
João Victor de Jesus - Módulo para criação e gerenciamento do labirinto.
"""

import random

def criar_labirinto(dificuldade: int = 1) -> list:
    """Cria um labirinto aleatório com base na dificuldade."""
    tamanho = dificuldade * 5 + 5
    labirinto = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
    for _ in range(tamanho * dificuldade):
        x, y = random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)
        labirinto[x][y] = '#'
    labirinto[0][0] = 'P'  # Ponto de partida
    labirinto[-1][-1] = 'S'  # Saída
    return labirinto

def imprimir_labirinto(labirinto: list) -> None:
    """Imprime o labirinto no terminal."""
    for linha in labirinto:
        print(''.join(linha))

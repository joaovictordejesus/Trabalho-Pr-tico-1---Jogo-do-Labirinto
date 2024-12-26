"""
João Victor de Jesus - Módulo para controle do jogador.
"""

from pynput.keyboard import Key, Listener

def iniciar_jogador() -> dict:
    """Inicializa o jogador na posição inicial."""
    return {'posicao': (0, 0), 'pontuacao': 0}

def mover(jogador: dict, labirinto: list) -> None:
    """Move o jogador com base na entrada do teclado."""
    def on_press(key):
        x, y = jogador['posicao']
        if key == Key.up:
            jogador['posicao'] = (max(x - 1, 0), y)
        elif key == Key.down:
            jogador['posicao'] = (min(x + 1, len(labirinto) - 1), y)
        elif key == Key.left:
            jogador['posicao'] = (x, max(y - 1, 0))
        elif key == Key.right:
            jogador['posicao'] = (x, min(y + 1, len(labirinto[0]) - 1))
        return False  # Para encerrar o listener

    with Listener(on_press=on_press) as listener:
        listener.join()

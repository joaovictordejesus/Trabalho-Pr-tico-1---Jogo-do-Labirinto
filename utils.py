"""
João Victor de Jesus - Módulo utilitário para o jogo.
"""

from rich.console import Console

console = Console()

def imprime_instrucoes():
    """Imprime as instruções do jogo."""
    console.print("Bem-vindo à Aventura no Labirinto!", style="bold blue")
    console.print("1. Use as setas do teclado para se mover.", style="green")
    console.print("2. Encontre a saída do labirinto ('S').", style="green")

def menu_principal():
    """Imprime o menu principal."""
    console.print("[1] Jogar", style="bold yellow")
    console.print("[2] Instruções", style="bold yellow")
    console.print("[3] Sair", style="bold yellow")

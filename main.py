"""
João Victor de Jesus - Script principal do jogo.
"""

import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover
from aventura_pkg.utils import imprime_instrucoes, menu_principal

def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument("--color", default="blue", help="Cor principal do jogo")
    parser.add_argument("--dificuldade", type=int, default=1, help="Nível de dificuldade") 
    args = parser.parse_args()

    print(f"Bem-vindo, {args.name}!")
    labirinto = criar_labirinto(args.dificuldade)
    jogador = iniciar_jogador()

    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                imprimir_labirinto(labirinto)
                mover(jogador, labirinto)
            case "2":
                imprime_instrucoes()
            case "3":
                print("Saindo do jogo...")
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()

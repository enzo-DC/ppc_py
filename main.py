
from game import logic, assets, utils



def main():
    player_wins = 0
    ia_wins = 0
    ties = 0

    utils.print_slow("Bienvenue au jeu Pierre-Papier-Ciseaux ! Tapez 'q' pour quitter à tout moment.", 0.01)

    while True:
        choice = utils.get_player_choice(assets.VALID_INPUTS)
        if choice == "quit":
            utils.print_slow("Merci d'avoir joué !", 0.01)
            break

        ia = logic.get_ia_choice(assets.CHOICES)
        result = logic.compare_choices(choice, ia)

        if result == 1:
            player_wins += 1
        elif result == -1:
            ia_wins += 1
        else:
            ties += 1

        utils.print_results(choice, ia, result, (player_wins, ia_wins, ties), assets.ICONS)

    
    print("=== Score final ===")
    print(f"Toi: {player_wins} | IA: {ia_wins} | Nuls: {ties}")
    print(f"Le Vainqueur est : {'Toi beau gosse 🔥💪 👑' if player_wins > ia_wins else 'L\'IA salle merde 💩 ☠' if ia_wins > player_wins else 'Aucun, c\'est une égalité 👀'}")


if __name__ == "__main__":
    main()

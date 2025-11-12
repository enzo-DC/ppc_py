import sys
import time
from typing import Dict, Tuple


def get_player_choice(valid_inputs: Dict[str, str]) -> str:
    prompt = "Ton choix (p/pierre, pa/papier, c/ciseaux) ou q pour quitter: "
    while True:
        print_slow(prompt, delay=0.03)
        raw = input()
        if raw is None:
            print("Warning: entrée vide, réessayez.")
            continue

        key = raw.strip().lower()
        if key == "":
            print("Warning: entrée vide, réessayez.")
            continue

        choice = valid_inputs.get(key)
        if choice is None:
            print("Warning: entrée invalide. Utilisez p/pierre, pa/papier, c/ciseaux ou q pour quitter.")
            continue

        return choice


def print_results(player: str, cpu: str, result: int, score: Tuple[int, int, int], icons: Dict[str, str]) -> None:
    p_icon = icons.get(player, "?")
    c_icon = icons.get(cpu, "?")

    if result == 1:
        msg = "Tu gagnes !"
    elif result == -1:
        msg = "Tu perds."
    else:
        msg = "Égalité."

    result_line = f"Tu: {player} {p_icon}  |  CPU: {cpu} {c_icon} -> {msg}"
    print_slow(result_line, delay=0.01)
    print(f"Score — Toi: {score[0]} | CPU: {score[1]} | Nuls: {score[2]}\n")


def print_slow(text: str, delay: float = 0.02) -> None:
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def write_text_file(path: str, contenu: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(contenu)


def read_text_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


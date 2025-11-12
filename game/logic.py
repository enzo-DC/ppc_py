import random
from typing import List, Tuple

RULES: List[Tuple[str, str]] = [
    ("pierre", "ciseaux"),
    ("ciseaux", "papier"),
    ("papier", "pierre"),
]


def get_ia_choice(choices: List[str]) -> str:
    return random.choice(choices)


def compare_choices(player: str, ia: str, rules: List[Tuple[str, str]] = RULES) -> int:
    if player == ia:
        return 0

    for winner, loser in rules:
        if player == winner and ia == loser:
            return 1
        if ia == winner and player == loser:
            return -1

    return -1

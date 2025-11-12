from typing import Dict, List

CHOICES: List[str] = ["pierre", "papier", "ciseaux"]

VALID_INPUTS: Dict[str, str] = {
    "p": "pierre",
    "pierre": "pierre",
    "pa": "papier",
    "papier": "papier",
    "c": "ciseaux",
    "ciseaux": "ciseaux",
    "q": "quit",
    "quit": "quit",
}

ICONS: Dict[str, str] = {
    "pierre": "🪨",   
    "papier": "📄",  
    "ciseaux": "✂️", 
}

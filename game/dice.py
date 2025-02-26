import random


def roll(notation: str) -> int:
    """
    Exemplo simplificado de rolagem: '1d20', '2d6', etc.
    """
    # Parse da string (muito básico, apenas exemplo)
    parts = notation.lower().split('d')
    qtd = int(parts[0])
    faces = int(parts[1])
    total = 0
    for _ in range(qtd):
        total += random.randint(1, faces)
    return total

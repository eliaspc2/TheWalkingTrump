import random


class direction:
    """Enumeração simples com as direções possíveis."""

    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4

    @classmethod
    def random(cls):
        """Retorna uma direção aleatória."""
        return random.randint(1, 4)

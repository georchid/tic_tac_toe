class GameFieldException(Exception):
    def __str__(self) -> str:
        return 'A value has been entered that is outside the playing field.'


class GameCellOccupaedError(Exception):
    def __str__(self) -> str:
        return 'Attempt to change occupied cell.'

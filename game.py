from gameparts import Board
from gameparts.exceptions import GameFieldException, GameCellOccupaedError


def main() -> None:
    game: Board = Board()
    game.display()
    current_player: str = 'X'
    running: bool = True
    while running:
        print(f'Ход делает {current_player}')

        while True:
            try:
                row: int = int(input('Enter the row number:'))
                if row < 0 or row >= game.field_size:
                    raise GameFieldException
                col: int = int(input('Enter the column number:'))
                if col < 0 or col >= game.field_size:
                    raise GameFieldException
                if game.board[row][col] != ' ':
                    raise GameCellOccupaedError
            except GameCellOccupaedError:
                print('The cell is occupied.')
                print('Enter other coordinates.')
            except GameFieldException as e:
                print(
                    e,
                    ('The range of the playing field '
                     f'is from 0 to {game.field_size - 1}')
                    )
                print('Please, enter the row and column again.')
            except ValueError:
                print('the value entered is not a number.',
                      'Please retry.')
            except Exception as e:
                print('An error occurred:', e)
            else:
                break

        game.make_move(row, col, current_player)
        game.display()

        if game.check_win(current_player):
            print(f'Победили {current_player}!')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()

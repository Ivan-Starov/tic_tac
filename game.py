from gameparts import Board
from gameparts.exceptions import FiledIndexError, СellOccupiedError

def main():

    game = Board()
    game.display()

    current_player = 'X'
    running = True
    while running:

        while True:
            try:
                
                row = int(input('Введите номер строки: '))

                if row < 0 or row >= game.field_size:
                    raise FiledIndexError

                col = int(input('Введите номер колонки: '))

                if col < 0 or col >= game.field_size:
                    raise FiledIndexError
                if game.board[row][col] != ' ':
                    raise СellOccupiedError

            except FiledIndexError:

                print(
                        f'Значение должно быть не отрицательным '
                        f'и меньше {game.field_size}'
                    )

                print(
                    'Пожалуйста введите значения для строки и столбца заново'
                )

                continue

            except ValueError:

                print('Буквы вводить нельзя. Только числа.')

                print(
                    'Пожалуйста введите значения для строки и столбца заново'
                )

                continue

            except СellOccupiedError:

                print('Попытка изменить ячейку которая занята.')

                continue

            except Exception as e:

                print(f'Возникла ошибка: {e}')

                continue

            else:

                break

        game.make_move(row, col, current_player)
        game.display()
        if game.empty_cells():
            print('Игра завершена! Ничья!')
            running = False
        elif game.check_win(current_player):
            print(f'Игра завершена! Победитель {current_player}!')
            running = False

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


if __name__ == '__main__':
    main()

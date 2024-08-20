class Board:
    """Класс описыващий игровое поле"""

    field_size = 3
    
    def __init__(self) -> None:
        """Инициализируется игровое поле"""
        self.board = [[' ' for _ in range(self.field_size)] 
                      for _ in range(self.field_size)]

    def make_move(self, row, col, player):
        """Изменяется значение клетки поля"""
        self.board[row][col] = player
    
    def display(self):
        for cell in self.board:
            print('|'.join(cell))
            print('-' * 5)
    
    def empty_cells(self):
        for rows in self.board:
            for col in rows:
                if col == ' ':
                    return False
        return True

    def check_win(self, player):
        for i in range(self.field_size):
            if (all([self.board[i][j] == player 
                     for j in range(self.field_size)]) or
                    all([self.board[j][i] == player
                         for j in range(self.field_size)])):
                return True

        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False

    def __str__(self) -> str:
        return (
            f'Объект игрового поля размером {self.field_size}x'
            f'{self.field_size}'
        )
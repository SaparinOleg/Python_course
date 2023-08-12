class ChessFigure:
    def __init__(self, color: str, file: int, rank: int):
        self.color = color
        self.file = file
        self.rank = rank

    def __str__(self):
        return f'{self.color} {self.__class__.__name__} on {(self.file, self.rank)}'

    def change_color(self) -> None:
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def is_valid_position(self, file: int, rank: int) -> bool:
        return True if 1 <= file <= 8 and 1 <= rank <= 8 else False

    def move(self, file: int, rank: int) -> None:
        if self.is_valid_position(file, rank):
            self.file = file
            self.rank = rank


class King(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for index in directions:
            file, rank = self.file + index[0], self.rank + index[1]
            if self.is_valid_position(file, rank):
                all_possible_moves.append((file, rank))
        return all_possible_moves


class Queen(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for index in directions:
            factor = 0
            while factor < 8:
                factor += 1
                file, rank = self.file + index[0] * factor, self.rank + index[1] * factor
                if self.is_valid_position(file, rank):
                    all_possible_moves.append((file, rank))
        return all_possible_moves


class Rook(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for index in directions:
            factor = 0
            while factor < 8:
                factor += 1
                file, rank = self.file + index[0] * factor, self.rank + index[1] * factor
                if self.is_valid_position(file, rank):
                    all_possible_moves.append((file, rank))
        return all_possible_moves


class Bishop(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        for index in directions:
            factor = 0
            while factor < 8:
                factor += 1
                file, rank = self.file + index[0] * factor, self.rank + index[1] * factor
                if self.is_valid_position(file, rank):
                    all_possible_moves.append((file, rank))
        return all_possible_moves


class Knight(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for index in directions:
            file, rank = self.file + index[0], self.rank + index[1]
            if self.is_valid_position(file, rank):
                all_possible_moves.append((file, rank))
        return all_possible_moves


class Pawn(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        if self.color == 'white':
            direction = 1
        else:
            direction = -1

        file, rank = self.file, self.rank + direction
        if self.is_valid_position(file, rank):
            all_possible_moves.append((self.file, self.rank + direction))

        if self.rank == 2 or self.rank == 7:
            file, rank = self.file, self.rank + direction * 2
            if self.is_valid_position(file, rank):
                all_possible_moves.append((file, rank))
        return all_possible_moves


def who_can_achieve(figures: list, coordinates: tuple):
    return [figure.__class__.__name__ for figure in figures if coordinates in figure.possible_moves()]


r11 = Rook('white', 1, 1)
n11 = Knight('white', 2, 1)
b11 = Bishop('white', 3, 1)
q1 = Queen('white', 4, 1)
k1 = King('white', 5, 1)
b12 = Bishop('white', 6, 1)
n12 = Knight('white', 7, 1)
r12 = Rook('white', 8, 1)
p11 = Pawn('white', 1, 2)
p12 = Pawn('white', 2, 2)
p13 = Pawn('white', 3, 2)
p14 = Pawn('white', 4, 2)
p15 = Pawn('white', 5, 2)
p16 = Pawn('white', 6, 2)
p17 = Pawn('white', 7, 2)
p18 = Pawn('white', 8, 2)

r21 = Rook('black', 1, 8)
n21 = Knight('black', 2, 8)
b21 = Bishop('black', 3, 8)
q2 = Queen('black', 4, 8)
k2 = King('black', 5, 8)
b22 = Bishop('black', 6, 8)
n22 = Knight('black', 7, 8)
r22 = Rook('black', 8, 8)
p21 = Pawn('black', 1, 7)
p22 = Pawn('black', 2, 7)
p23 = Pawn('black', 3, 7)
p24 = Pawn('black', 4, 7)
p25 = Pawn('black', 5, 7)
p26 = Pawn('black', 6, 7)
p27 = Pawn('black', 7, 7)
p28 = Pawn('black', 8, 7)

chess_figures = [r11, n11, b11, q1, k1, b12, n12, r12, p11, p12, p13, p14, p15, p16, p17, p18,
                 r21, n21, b21, q2, k2, b22, n22, r22, p21, p22, p23, p24, p25, p26, p27, p28]
position = (2, 2)

print()
print("Can move to a given position:")
print(who_can_achieve(chess_figures, position))

print()
print(p24)
print(p16)
print(k1)
print(n22)

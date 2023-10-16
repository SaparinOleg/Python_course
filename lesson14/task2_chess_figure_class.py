class ChessFigure:
    color = 'black'
    file = 1
    rank = 1

    def change_color(self) -> None:
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def is_valid_position(self, file: int, rank: int) -> bool:
        return 0 <= file <= 7 and 0 <= rank <= 7

    def move(self, file: int, rank: int) -> None:
        if self.is_valid_position(file, rank):
            self.file = file
            self.rank = rank


class King(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for index in directions:
            if self.is_valid_position(self.file + index[0], self.rank + index[1]):
                all_possible_moves.append((self.file + index[0], self.rank + index[1]))
        return all_possible_moves


class Queen(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for index in directions:
            factor = 0
            while factor < 8:
                factor += 1
                if self.is_valid_position(self.file + index[0] * factor, self.rank + index[1] * factor):
                    all_possible_moves.append((self.file + index[0] * factor, self.rank + index[1] * factor))
        return all_possible_moves


class Rook(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for index in directions:
            factor = 0
            while factor < 8:
                factor += 1
                if self.is_valid_position(self.file + index[0] * factor, self.rank + index[1] * factor):
                    all_possible_moves.append((self.file + index[0] * factor, self.rank + index[1] * factor))
        return all_possible_moves


class Bishop(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        for index in directions:
            factor = 0
            while factor < 8:
                factor += 1
                if self.is_valid_position(self.file + index[0] * factor, self.rank + index[1] * factor):
                    all_possible_moves.append((self.file + index[0] * factor, self.rank + index[1] * factor))
        return all_possible_moves


class Knight(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for index in directions:
            if self.is_valid_position(self.file + index[0], self.rank + index[1]):
                all_possible_moves.append((self.file + index[0], self.rank + index[1]))
        return all_possible_moves


class Pawn(ChessFigure):
    def possible_moves(self) -> list:
        all_possible_moves = []
        if self.color == 'white':
            direction = 1
        else:
            direction = -1

        if self.is_valid_position(self.file, self.rank + direction):
            all_possible_moves.append((self.file, self.rank + direction))

        if self.rank == 2 or self.rank == 7:
            if self.is_valid_position(self.file, self.rank + direction * 2):
                all_possible_moves.append((self.file, self.rank + direction * 2))
        return all_possible_moves


def who_can_achieve(figures: list, coordinates: tuple):
    return [figure.__class__.__name__ for figure in figures if coordinates in figure.possible_moves()]


k = King()
q = Queen()
r = Rook()
b = Bishop()
n = Knight()
p = Pawn()
print('Possible moves from this position:')
print(f' King: {k.possible_moves()}')
print(f' Queen: {q.possible_moves()}')
print(f' Rook: {r.possible_moves()}')
print(f' Bishop: {b.possible_moves()}')
print(f' Knight: {n.possible_moves()}')
print(f' Pawn: {p.possible_moves()}')

chess_figures = [k, q, r, b, n, p]
position = (1, 2)
p.change_color()
print()
print(f'From position: {(ChessFigure.file, ChessFigure.rank)}, position: {position} can achieve:')
print(who_can_achieve(chess_figures, position))

import colorama
from colorama import Fore
from colorama import Back
from colorama import Style

colorama.init()

WHITE = 1
BLACK = 2


class ChessPiece:
    name: str

    def __init__(self, color: int, cell: str):
        self.color = color
        file = sorted((0, ord(cell[0]) - 97, 7))[1]
        rank = sorted((0, int(cell[1:]) - 1, 7))[1]
        self.file = ord(cell[0]) - 97
        self.rank = int(cell[1:]) - 1

    def __str__(self):
        color = Fore.BLACK if self.color == 1 else Fore.WHITE
        background = Back.WHITE if self.color == 1 else Back.BLACK
        files = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return f'{color}{background}{self.name}{files[self.file]}{self.rank + 1}{Style.RESET_ALL}'

    def __repr__(self):
        return self.__str__()

    def change_color(self) -> None:
        self.color = BLACK if self.color == WHITE else WHITE

    @staticmethod
    def try_move(file: int, rank: int) -> bool:
        return 0 <= file <= 7 and 0 <= rank <= 7

    def move(self, file: int, rank: int) -> None:
        if self.try_move(file, rank):
            self.file = file
            self.rank = rank


class King(ChessPiece):
    name = 'K'

    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for file_d, rank_d in directions:
            file = self.file + file_d
            rank = self.rank + rank_d
            if self.try_move(file, rank):
                all_possible_moves.append((file, rank))
        return all_possible_moves


class Queen(ChessPiece):
    name = 'Q'

    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for file_d, rank_d in directions:
            for factor in range(1, 8):
                file = self.file + file_d * factor
                rank = self.rank + rank_d * factor
                if self.try_move(file, rank):
                    all_possible_moves.append((file, rank))
                else: break
        return all_possible_moves


class Rook(ChessPiece):
    name = 'R'

    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for file_d, rank_d in directions:
            for factor in range(1, 8):
                file = self.file + file_d * factor
                rank = self.rank + rank_d * factor
                if self.try_move(file, rank):
                    all_possible_moves.append((file, rank))
                else: break
        return all_possible_moves


class Bishop(ChessPiece):
    name = 'B'

    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        for file_d, rank_d in directions:
            for factor in range(1, 8):
                file = self.file + file_d * factor
                rank = self.rank + rank_d * factor
                if self.try_move(file, rank):
                    all_possible_moves.append((file, rank))
                else: break
        return all_possible_moves


class Knight(ChessPiece):
    name = 'N'

    def possible_moves(self) -> list:
        all_possible_moves = []
        directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for file_d, rank_d in directions:
            file = self.file + file_d
            rank = self.rank + rank_d
            if self.try_move(file, rank):
                all_possible_moves.append((file, rank))
        return all_possible_moves


class Pawn(ChessPiece):
    name = ''

    def possible_moves(self) -> list:
        all_possible_moves = []
        direction = 1 if self.color == WHITE else -1

        file = self.file
        rank = self.rank + direction
        if self.try_move(file, rank):
            all_possible_moves.append((self.file, self.rank + direction))

        if self.rank == 1 or self.rank == 6:
            file = self.file
            rank = self.rank + direction * 2
            if self.try_move(file, rank):
                all_possible_moves.append((file, rank))
        return all_possible_moves


def who_can_reach(pieces: list, coordinates: tuple):
    return [piece for piece in pieces if coordinates in piece.possible_moves()]


r11 = Rook(WHITE, 'a1')
n11 = Knight(WHITE, 'b1')
b11 = Bishop(WHITE, 'c1')
q1 = Queen(WHITE, 'd1')
k1 = King(WHITE, 'e1')
b12 = Bishop(WHITE, 'f1')
n12 = Knight(WHITE, 'g1')
r12 = Rook(WHITE, 'h1')
p11 = Pawn(WHITE, 'a2')
p12 = Pawn(WHITE, 'b2')
p13 = Pawn(WHITE, 'c2')
p14 = Pawn(WHITE, 'd2')
p15 = Pawn(WHITE, 'e2')
p16 = Pawn(WHITE, 'f2')
p17 = Pawn(WHITE, 'g2')
p18 = Pawn(WHITE, 'h2')

r21 = Rook(BLACK, 'a8')
n21 = Knight(BLACK, 'b8')
b21 = Bishop(BLACK, 'c8')
q2 = Queen(BLACK, 'd8')
k2 = King(BLACK, 'e8')
b22 = Bishop(BLACK, 'f8')
n22 = Knight(BLACK, 'g8')
r22 = Rook(BLACK, 'h8')
p21 = Pawn(BLACK, 'a7')
p22 = Pawn(BLACK, 'b7')
p23 = Pawn(BLACK, 'c7')
p24 = Pawn(BLACK, 'd7')
p25 = Pawn(BLACK, 'e7')
p26 = Pawn(BLACK, 'f7')
p27 = Pawn(BLACK, 'g7')
p28 = Pawn(BLACK, 'h7')

chess_pieces = [r11, n11, b11, q1, k1, b12, n12, r12, p11, p12, p13, p14, p15, p16, p17, p18,
                r21, n21, b21, q2, k2, b22, n22, r22, p21, p22, p23, p24, p25, p26, p27, p28]
position = (3, 7)

print()
print("Can move to a given position:")
print(who_can_reach(chess_pieces, position))

print()
print(chess_pieces)

print()
print(p11)
print(k1)
print(k2)
print(r22)
print(n12)
print(p25)

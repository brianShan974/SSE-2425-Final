from enum import Enum
from typing import Optional
from abc import ABC, abstractmethod

from grid import Grid


class ChessPiece(ABC):
    __slots__ = ("_x", "_y")

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def move_by(self, dx, dy) -> tuple[int, int]:
        x = self._x + dx
        y = self._y + dy
        return (x, y)

    @abstractmethod
    def get_possible_pos(
        self, grid: Optional[Grid] = None
    ) -> Optional[list[tuple[int, int]]]:
        return None


class King(ChessPiece):
    def get_possible_pos(
        self, grid: Optional[Grid] = None
    ) -> Optional[list[tuple[int, int]]]:
        moves = []
        dx_dy_range = (-1, 0, 1)
        for dx in dx_dy_range:
            for dy in dx_dy_range:
                if not dx == dy == 0:
                    moves.append(self.move_by(dx, dy))
        return moves


class Castle(ChessPiece):
    def get_possible_pos(
        self, grid: Optional[Grid] = None
    ) -> Optional[list[tuple[int, int]]]:
        return super().get_possible_pos(grid)


class Bishop(ChessPiece):
    def get_possible_pos(self) -> Optional[list[tuple[int, int]]]:
        return super().get_possible_pos()


class Queen(ChessPiece):
    def get_possible_pos(self) -> Optional[list[tuple[int, int]]]:
        return super().get_possible_pos()


class Knight(ChessPiece):
    def get_possible_pos(self) -> Optional[list[tuple[int, int]]]:
        moves = []
        dx_dy_range = (2, -2, 1, -1)
        for dx in dx_dy_range:
            for dy in dx_dy_range:
                if abs(dx) != abs(dy):
                    moves.append(self.move_by(dx, dy))
        return moves


class Pawn(ChessPiece):
    def get_possible_pos(self) -> Optional[list[tuple[int, int]]]:
        return super().get_possible_pos()

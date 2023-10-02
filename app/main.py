from __future__ import annotations


class Distance:

    def __init__(self, km: float | int) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        return Distance(km=self.km + other)

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, number: int) -> "Distance":
        return Distance(km=self.km * number)

    def __truediv__(self, number: int) -> "Distance":
        return Distance(km=round(self.km / number, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return not self.km > other.km
        return not self.km > other

    def __ge__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            return not self.km < other.km
        return not self.km < other

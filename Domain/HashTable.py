from typing import Tuple


class HashTable:
    def __init__(self, size):
        self._items = [[] for _ in range(size)]
        self._size = size

    def hash(self, key) -> int:
        key = sum(ord(char) - ord('0') for char in key)
        return key % self._size

    def add(self, key) -> Tuple[int, int]:
        if self.contains(key):
            return self.getPosition(key)
        try:
            nonePos = self._items[self.hash(key)].index(None)
            self._items[self.hash(key)][nonePos] = key
        except ValueError:
            self._items[self.hash(key)].append(key)
        return self.getPosition(key)

    def contains(self, key) -> bool:
        return self.getPosition(key) != (-1, -1)

    def remove(self, key) -> None:

        pos = self.getPosition(key)
        if pos[0] == -1:
            return
        self._items[pos[0]][pos[1]] = None

    def __str__(self) -> str:
        result = "Symbol Table (kept as a Hash Table using Lists)\n"
        for i in range(self._size):
            result = result + str(i) + "->" + str(self._items[i]) + "\n"
        return result

    def getPosition(self, key) -> Tuple[int, int]:
        list_position = self.hash(key)
        try:
            list_index = self._items[list_position].index(key)
            return list_position, list_index
        except ValueError:
            return -1, -1

    def getKeyByPosition(self, position: Tuple[int, int]):
        return self._items[position[0]][position[1]]
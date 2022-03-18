from abc_constructor import Constructor
from tile import Tile


class TileConstructor(Constructor):
    def __init__(self, level):
        super().__init__(['x'], ['object'], level)
        self.__sprites_dict = {'x': 'brick.png'}

    def instantiate(self, x, y, tag):
        self.__init__(self._level)
        SIZE = self._config.get('tile-size')
        if tag in self.__sprites_dict.keys():
            wall = Tile(x*SIZE, y*SIZE, SIZE,
                        f'sprites/{self.__sprites_dict[tag]}')
            self._lists.append('obstacle')
            return wall

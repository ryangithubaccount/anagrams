import random
class bag:
    def __init__(self):
        self.tiles = []
        self.tiles += ['A'] * 9
        self.tiles += ['B'] * 2
        self.tiles += ['C'] * 2
        self.tiles += ['D'] * 4
        self.tiles += ['E'] * 12
        self.tiles += ['F'] * 2
        self.tiles += ['G'] * 3
        self.tiles += ['H'] * 2
        self.tiles += ['I'] * 9
        self.tiles += ['J'] * 1
        self.tiles += ['K'] * 2
        self.tiles += ['L'] * 4
        self.tiles += ['M'] * 2
        self.tiles += ['N'] * 6
        self.tiles += ['O'] * 8
        self.tiles += ['P'] * 2
        self.tiles += ['Q'] * 1
        self.tiles += ['R'] * 6
        self.tiles += ['S'] * 4
        self.tiles += ['T'] * 6
        self.tiles += ['U'] * 4
        self.tiles += ['V'] * 2
        self.tiles += ['W'] * 2
        self.tiles += ['X'] * 1
        self.tiles += ['Y'] * 2
        self.tiles += ['Z'] * 1
        random.shuffle(self.tiles)
    
    def draw(self):
        if len(self.tiles) == 0:
            return None
        tile = self.tiles[0]
        self.tiles = self.tiles[1:]
        return tile
    
    def add(self, tile):
        idx = random.randint(0, len(self.tiles))
        self.tiles.insert(idx, tile)


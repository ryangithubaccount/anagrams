import random
class bag:
    # The bag of tiles for a scrabble game
    # The numbers are how many of each tile there are
    def __init__(self):
        self.tiles = []
        self.tiles += ['A'] * 5
        self.tiles += ['B'] * 3
        self.tiles += ['C'] * 2
        self.tiles += ['D'] * 4
        self.tiles += ['E'] * 5
        self.tiles += ['F'] * 2
        self.tiles += ['G'] * 3
        self.tiles += ['H'] * 2
        self.tiles += ['I'] * 5
        self.tiles += ['J'] * 1
        self.tiles += ['K'] * 1
        self.tiles += ['L'] * 4
        self.tiles += ['M'] * 3
        self.tiles += ['N'] * 5
        self.tiles += ['O'] * 5
        self.tiles += ['P'] * 2
        self.tiles += ['Q'] * 1
        self.tiles += ['R'] * 3
        self.tiles += ['S'] * 2
        self.tiles += ['T'] * 3
        self.tiles += ['U'] * 5
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


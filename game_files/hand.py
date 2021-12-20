class hand:
    # A scrabble hand (7 tiles usually)
    def __init__(self, s):
        self.tiles = []
        for i in s:
            self.tiles.append(i)
    
    def get_letters(self):
        return self.tiles

    def add_tile(self, tile):
        self.tiles.append(tile)

    def remove_tile(self, tile):
        self.tiles.remove(tile)
import os
import random

class hand:
    # A scrabble hand (7 tiles usually)
    def __init__(self, num, tiles=None):
        if not tiles:
            script_dir = os.path.dirname(__file__)
            rel_path = '../dictionaries/' + str(num) + '_letters.txt'
            abs_file_path = os.path.join(script_dir, rel_path)
            f = open(abs_file_path, 'r')
            text = f.readlines()
            idx = random.randint(0, len(text) - 1)
            self.tiles = list(text[idx][:-1])
            random.shuffle(self.tiles)
        else:
            self.tiles = tiles
    
    def get_letters(self):
        return self.tiles

    def add_tile(self, tile):
        self.tiles.append(tile)

    def remove_tile(self, tile):
        self.tiles.remove(tile)

    def shuffle(self):
        random.shuffle(self.tiles)
        return self.tiles
import word_list as word_list
import hand as hand
import bag as bag
import time
import random

class anagrams:
    # A basic set-up of a scrabble game
    def __init__(self):
        self.word_list = word_list.word_list()
        self.bag = bag.bag()
        temp = ''
        for _ in range(6):
            temp += self.bag.draw()
        self.hand = hand.hand(temp)
        self.score = 0
        self.used_words = []
        self.valid_words = {}
        self.generate_possible_words()

    def score_word(self, word):
        if len(word) <= 2:
            return
        try:
            if not self.valid_words[word.upper()]:
                self.used_words.append(word)
                self.valid_words[word.upper()] = True
                if len(word) == 3:
                    self.score += 100
                elif len(word) == 4:
                    self.score += 400
                elif len(word) == 5:
                    self.score += 800
                else:
                    self.score += 1200
        except KeyError:
            return

    def generate_possible_words(self):
        # Finds possible permutations and tests if they are valid words
        hand = self.hand.get_letters()
        possible_permutations = []
        for i in range(3, len(hand) + 1):
            possible_permutations += generate_permutations(hand, i)
        result = set()
        for perm in possible_permutations:
            if (self.word_list.check_if_valid(perm)):
                self.valid_words[perm] = False
    
    def get_hand(self):
        return self.hand.get_letters()

    def get_word_list(self):
        return self.word_list.get_list()

    def get_score(self):
        return self.score
    
    def get_valid_words(self):
        return self.valid_words
    
    def get_used_words(self):
        return self.used_words

def generate_permutations(tiles, num):
    # Uses recursion to generate possible permutations
    if num == 1:
        return tiles
    else:
        result = []
        for i in range(len(tiles)):
            prev_perm = generate_permutations(tiles[0:i] + tiles[i + 1:], num - 1)
            for elem in prev_perm:
                result.append(tiles[i] + elem)
    return result



game = anagrams()
print("Welcome to anagrams!")
start_prompt = input("Press Y to start: ")
while start_prompt.lower() != 'y':
    start_prompt = input("Invalid input. Press Y to start: ")
start_time = time.time()
print("\nSTART")
while time.time() < start_time + 10:
    print(game.get_hand())
    word = input("Enter a word: ")
    game.score_word(word)
    print()
print("END\n")
print("Congratulations, your final score was: " + str(game.get_score()))
print("Your valid words were:")
print(game.get_used_words())

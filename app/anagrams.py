import importlib.util
spec=importlib.util.spec_from_file_location("word_list","app/word_list.py")
word_list = importlib.util.module_from_spec(spec)
spec.loader.exec_module(word_list)

spec=importlib.util.spec_from_file_location("hand","app/hand.py")
hand = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hand)
import time

class anagrams:
    # A basic set-up of a anagrams game
    def __init__(self, time, num_tiles):
        self.word_list = word_list.word_list()
        self.num_tiles = num_tiles
        self.time = time
        self.hand = hand.hand(num_tiles)
        self.score = 0
        self.used_words = []
        self.valid_words = {}
        self.generate_possible_words()

    def score_word(self, word):
        # 0 means invalid word, 1 means already used, 2 means valid word
        if len(word) <= 2:
            return 0
        try:
            if not self.valid_words[word]:
                self.used_words.append(word)
                self.valid_words[word] = True
                if len(word) == 3:
                    self.score += 100
                else:
                    self.score += 400 * (len(word) - 3)
                return 2
            return 1
        except KeyError:
            return 0

    def generate_possible_words(self):
        # Finds possible permutations and tests if they are valid words
        hand = self.hand.get_letters()
        possible_permutations = generate_permutations(hand, len(hand))
        for i in possible_permutations:
            for perm in i:
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
    
    def get_time(self):
        return self.time

    def shuffle(self):
        self.hand.shuffle()
        return self.get_hand()

def generate_permutations(tiles, num):
    # Uses recursion to generate possible permutations
    if num == 1:
        return tiles
    else:
        result = []
        prev = []
        prev.append(tiles)
        for i in range(num - 1):
            prev.append(set())
        for i in range(len(tiles)):
            prev_perm = generate_permutations(tiles[0:i] + tiles[i + 1:], num - 1)
            for j in range(1, len(prev_perm)):
                for perm in prev_perm[j]:
                    prev[j].add(perm)
            for perm in prev_perm[-1]:
                result.append(tiles[i] + perm)
        prev.append(result)
    return prev


# CTRL + '/' will let you uncomment 

# print("Welcome to anagrams!")

# start_prompt = input("Press Y to start, Q to quit: ")
# while start_prompt.upper() != 'Y' and start_prompt.upper() != 'Q':
#     start_prompt = input("Invalid input. Press Y to start, Q to quit: ")
# if start_prompt.upper() == 'Q':
#     exit(0)

# game_time = input("How much time do you want (10s - 300s): ")
# while not game_time.isnumeric() or int(game_time) < 10 or int(game_time) > 300:
#     game_time = input("Invalid time. How much time do you want (10s - 300s): ")
# num_tiles = input("How many tiles do you want (6 - 9): ")
# while not game_time.isnumeric() or int(num_tiles) < 6 or int(num_tiles) > 10:
#     num_tiles = input("Invalid number of tiles. How many tiles do you want (6 - 9): ")
# game = anagrams(int(game_time), int(num_tiles))

# start_time = time.time()
# print("\nSTART")
# while time.time() < start_time + game.get_time():
#     print(game.get_hand())
#     word = input("Enter a word: ").upper()
#     game.score_word(word)
#     print()
# print("END\n")
# print("Congratulations, your final score was: " + str(game.get_score()) + "!")
# print("Your valid words were:")
# print(game.get_used_words())
# print("All possible words were:")
# print(list(game.get_valid_words().keys()))

import scrabble_board as scrabble_board
import word_list as word_list
import hand as hand
import bag as bag
import random

class game:
    def __init__(self):
        self.board = scrabble_board.scrabble_board()
        self.word_list = word_list.word_list()
        self.bag = bag.bag()
        temp = ''
        for _ in range(7):
            temp += self.bag.draw()
        self.hand = hand.hand(temp)
        self.tile_scores = {}
        for i in 'ZQ':
            self.tile_scores[i] = 10
        for i in 'JX':
            self.tile_scores[i] = 8
        for i in 'K':
            self.tile_scores[i] = 5
        for i in 'FHVWY':
            self.tile_scores[i] = 4
        for i in 'BCMP':
            self.tile_scores[i] = 3
        for i in 'DG':
            self.tile_scores[i] = 2
        for i in 'AEILNORSTU':
            self.tile_scores[i] = 1
        self.tile_scores['_'] = 0

    def score_word(self, word):
        score = 0
        for i in word:
            score += self.tile_scores[i]
        return score

    def generate_possible_words(self):
        hand = self.hand.get_letters()
        possible_permutations = []
        for i in range(2, len(hand) + 1):
            possible_permutations += generate_permutations(hand, i)
        result = set()
        for perm in possible_permutations:
            if (self.word_list.check_if_valid(perm)):
                result.add(perm)
        return result

    def generate_possible_words2(self):
        available = self.board.get_available_spots()
        hand = self.get_hand()
        possible_permutations = []
        result = set()
        for i in range(1, len(hand) + 1):
            possible_permutations += generate_permutations(hand, i)
        for spot in available:
            # left, right, up, down mean which way the word is extending from the spot
            # ie) let * = spot, then *lol would be right (although there would also be a letter on spot)
            left = self.board.calculate_border(spot[0], spot[1], (-1, 0))
            right = self.board.calculate_border(spot[0], spot[1], (1, 0))
            up = self.board.calculate_border(spot[0], spot[1], (0, 1))
            down = self.board.calculate_border(spot[0], spot[1], (0, -1))
            for i in range(left[0]):
                add_on_front = ''
                add_on_end = ''
                if right[0] == 1:
                    add_on_end = right[1]
                for perm in possible_permutations[i + 1]:
                    if i + 1 == left[0]:
                        add_on_front = left[1]
                    temp = add_on_front + perm + add_on_end
                    if self.word_list.check_if_valid(temp):
                        result.add(temp, (spot[0] - i, spot[1]))
        return result
    
    def best_word_in_hand(self):
        words = self.generate_possible_words()
        best_word = ""
        max = 0
        for i in words:
            temp = self.score_word(i)
            if temp > max:
                max = temp
                best_word = i
        return (best_word, max)
    
    def get_hand(self):
        return self.hand.get_letters()

    def get_word_list(self):
        return self.word_list.get_list()

def generate_permutations(tiles, num):
    if num == 1:
        return tiles
    else:
        result = []
        for i in range(len(tiles)):
            prev_perm = generate_permutations(tiles[0:i] + tiles[i + 1:], num - 1)
            for elem in prev_perm:
                result.append(tiles[i] + elem)
    return result

def run_game():
    new_game = game()
    hand = new_game.get_hand()
    print(hand)
    new_game.board.add_letters(0, 0, 0, 'BLANK')
    #new_game.board.add_letters(0, -5, 1, 'BADUMP')
    new_game.board.print_board()
    print(new_game.generate_possible_words2())
    #print(new_game.board.get_available_spots())
    #print("best word is:")
    #best_word = new_game.best_word_in_hand()
    #print(best_word[0] + " with a score of " + str(best_word[1]))

run_game()

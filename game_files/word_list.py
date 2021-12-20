import os

class word_list:
    # Making a list of valid words
    # The "list" is a dictionary that is indexed by keys of two letters
    # ie) the keys are 'aa', 'ab', 'ac', ... 'zy', 'zz'
    # For each key, it gives the words that start with these letters
    def __init__(self):
        self.lists = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter1 in alphabet:
            for letter2 in alphabet:
                script_dir = os.path.dirname(__file__)
                rel_path = "../dictionaries/" + letter1 + "/" + letter1 + "_" + letter2 + ".txt"
                abs_file_path = os.path.join(script_dir, rel_path)
                temp = []
                f = open(abs_file_path, 'r')
                temp = f.readlines()
                f.close()
                self.lists[letter1 + letter2] = temp

    def check_if_valid(self, word):
        word = word.lower()
        try:
            for i in self.lists[word[:2]]:
                if i[:-1] == word:
                    return True
                if i[:-1] > word:
                    return False
            return False
        except KeyError:
            return False

    def get_list(self):
        return self.lists

import os

class word_list:
    # Making a list of valid words
    # The "list" is a dictionary that is indexed by keys of two letters
    # ie) the keys are 'aa', 'ab', 'ac', ... 'zy', 'zz'
    # For each key, it gives the words that start with these letters
    def __init__(self, lists=None):
        if not lists:
            self.lists = {}
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            for letter1 in alphabet:
                for letter2 in alphabet:
                    for letter3 in alphabet:
                        script_dir = os.path.dirname(__file__)
                        rel_path = "../dictionaries/" + letter1 + "/" + letter1 + "_" + letter2 + "_" + letter3 + ".txt"
                        abs_file_path = os.path.join(script_dir, rel_path)
                        temp = []
                        f = open(abs_file_path, 'r')
                        temp = f.readlines()
                        f.close()
                        self.lists[letter1.upper() + letter2.upper() + letter3.upper()] = temp
        else:
            self.lists = lists

    def check_if_valid(self, word):
        try:
            for i in self.lists[word[:3]]:
                if i[:-1] == word:
                    return True
                if i[:-1] > word:
                    return False
            return False
        except KeyError:
            return False

    def get_list(self):
        return self.lists

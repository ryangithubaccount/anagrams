import os

class word_list:
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
                for line in f:
                    temp.append(f.readline()[:-1])
                f.close()
                self.lists[letter1 + letter2] = temp

    def check_if_valid(self, word):
        word = word.lower()
        try:
            for i in self.lists[word[:2]]:
                if i == word:
                    return True
                if i > word:
                    return False
            return False
        except KeyError:
            return False

    def get_list(self):
        return self.lists

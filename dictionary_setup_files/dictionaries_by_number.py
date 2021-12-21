import os

alphabet = 'abcdefghijklmnopqrstuvwxyz'
script_dir = os.path.dirname(__file__)
for i in range(6, 11):
    rel_path = '../dictionaries/' + str(i) + '_letters.txt'
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path, 'w')

    for letter in alphabet:
        rel_path2 = '../dictionaries/' + letter + '.txt'
        abs_file_path2 = os.path.join(script_dir, rel_path2)
        f2 = open(abs_file_path2, 'r')
        text = f2.readline()
        while len(text) <= i + 1:
            if len(text) == i + 1:
                f.write(text.upper())
            text = f2.readline()
        f2.close()
    f.close()
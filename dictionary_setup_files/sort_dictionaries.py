import os

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    script_dir = os.path.dirname(__file__)
    rel_path1 = "../dictionaries/" + letter + ".txt"
    abs_file_path1 = os.path.join(script_dir, rel_path1)
    f = open(abs_file_path1, 'r')
    total_text = []
    text = f.readline()
    while text:
        total_text.append(text)
        text = f.readline()
    total_text.sort()
    f.close()
    rel_path2 = "../dictionaries/" + letter + "_sorted.txt"
    abs_file_path2 = os.path.join(script_dir, rel_path2)
    f = open(abs_file_path2, 'w')
    for i in total_text:
        f.write(i)
    f.close()
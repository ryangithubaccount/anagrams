import os

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter1 in alphabet:
    script_dir = os.path.dirname(__file__)
    rel_path1 = "../dictionaries/" + letter1 + "_sorted.txt"
    abs_file_path1 = os.path.join(script_dir, rel_path1)
    source = open(abs_file_path1, 'r')
    text = source.readline()
    
    for letter2 in alphabet:
        for letter3 in alphabet:
            rel_path2 = "../dictionaries/" + letter1 + "/" + letter1 + "_" + letter2 + "_" + letter3 + ".txt"
            abs_file_path2 = os.path.join(script_dir, rel_path2)
            sub_dictionary = open(abs_file_path2, "w")
            while text:
                if len(text) >= 4:
                    if text[1:3] == letter2 + letter3:
                        sub_dictionary.write(text.upper())
                    else:
                        break
                text = source.readline()
            sub_dictionary.close()
    source.close()
        
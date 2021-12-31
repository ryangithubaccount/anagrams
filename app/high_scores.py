import os

def check_high_scores(score, letters):
    hand = ''
    for l in letters:
        hand += l
    script_dir = os.path.dirname(__file__)
    rel_path = "static/high_scores.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path, 'r')
    scores = []
    x = f.readlines()
    for i in  x:
        scores.append(i[:-1].split(' ', 1))
    if ([str(score), hand] not in scores):
        scores.append([str(score), hand])
    scores = sorted(scores, key = lambda x:int(x[0]), reverse=True)
    f.close()
    f = open(abs_file_path, 'w')
    i = 0
    while i < 5 and i < len(scores):
        f.write(scores[i][0] + ' ' + scores[i][1] + '\n')
        i += 1
    f.close()
    for i in range(5):
        if scores[i] == [str(score), hand]:
            break
    # i is the index of it
    return scores[:5], i

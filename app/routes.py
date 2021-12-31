from flask import Flask, render_template, request, url_for, flash, redirect, session
from app import app
import time
import app.anagrams as anagrams
from app.high_scores import check_high_scores

game_instance = [None]

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        num_tiles = int(request.form['tiles'])
        num_seconds = int(request.form['seconds'])
        if num_tiles < 6 or num_tiles > 9:
            return render_template("index.html", error="Please enter a valid tile range (6-9 tiles)")
        elif num_seconds < 30 or num_seconds > 90:
            return render_template("index.html", error="Please enter a valid time range (30-90 seconds)")
        else:
            game_instance[0] = anagrams.anagrams(num_seconds, num_tiles)
            session['start_time'] = time.time()
            return redirect(url_for('game'))
    return render_template("index.html")


@app.route("/game", methods=('GET', 'POST'))
def game():
    hand = game_instance[0].get_hand()
    game_time = game_instance[0].get_time()
    score = str(game_instance[0].get_score())
    typed_words = game_instance[0].get_used_words()
    num_typed = len(typed_words)
    if request.method == 'POST':
        # add to database
        
        if request.form['action'] == 'shuffle':
            hand = game_instance[0].shuffle()
            return render_template("game.html", time=game_time - int(time.time()-session.get('start_time')), hand=hand, score=score, typed_words=typed_words[::-1], num_typed=num_typed, result=3)
        elif request.form['action'] == 'quit':
            return redirect(url_for('endgame'))
        else:
            word = request.form['input'].upper()
            result = game_instance[0].score_word(word)
            added_score = game_instance[0].get_score() - int(score)
            score = str(game_instance[0].get_score())
            typed_words = game_instance[0].get_used_words()
            num_typed = len(typed_words)
            return render_template("game.html", time=game_time - int(time.time()-session.get('start_time')), hand=hand, score=score, typed_words=typed_words[::-1], num_typed=num_typed, result=result, added_score=added_score)
    return render_template("game.html", time=game_time, hand=hand, score=score, typed_words=typed_words, num_typed=num_typed, result=3)

@app.route("/endgame", methods=('GET', 'POST'))
def endgame():
    typed_words = game_instance[0].get_used_words()
    num_typed = len(typed_words)
    final_score = str(game_instance[0].get_score())
    all_words = game_instance[0].get_valid_words()
    
    high_scores, success = check_high_scores(int(final_score), game_instance[0].get_hand())

    words = list(all_words.keys())
    words.reverse()
    shown_words = words
    hidden_words = []
    if len(words) > 10:
        shown_words = words[:10]
        hidden_words = words[10:]
    return render_template("endgame.html", typed_words=typed_words, final_score=final_score, all_words=all_words, shown_words=shown_words, hidden_words=hidden_words,  num_typed=num_typed, high_scores=high_scores, success=success)

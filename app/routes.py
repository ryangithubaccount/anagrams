from flask import Flask, render_template, request, url_for, flash, redirect, session
from app import app
import app.anagrams as anagrams

game_instance = [None]

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        num_tiles = request.form['tiles']
        num_seconds = request.form['seconds']
        game_instance[0] = anagrams.anagrams(num_seconds, num_tiles)
        return redirect(url_for('game'))
    return render_template("index.html")


@app.route("/game", methods=('GET', 'POST'))
def game():
    hand = game_instance[0].get_hand()
    time = game_instance[0].get_time()
    score = str(game_instance[0].get_score())
    typed_words = game_instance[0].get_used_words()
    if request.method == 'POST':
        # add to database 
        word = request.form['userTyped'].upper()
        game_instance[0].score_word(word)
        score = str(game_instance[0].get_score())
        typed_words = game_instance[0].get_used_words()
        return render_template("game.html", time=time, hand=hand, score=score, typed_words=typed_words)
    return render_template("game.html", time=time, hand=hand, score=score, typed_words=typed_words)

@app.route("/endgame", methods=('GET', 'POST'))
def endgame():
    typed_words = game_instance[0].get_used_words()
    final_score = str(game_instance[0].get_score())
    all_words = list(game_instance[0].get_valid_words().keys())
    return render_template("endgame.html", typed_words=typed_words, final_score=final_score, all_words=all_words)

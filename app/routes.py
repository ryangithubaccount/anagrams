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
    if request.method == 'POST':
        # add to database 
        return None
    return render_template("game.html", time=time, hand=hand)

@app.route("/endgame", methods=('GET', 'POST'))
def endgame():
    return render_template("endgame.html")

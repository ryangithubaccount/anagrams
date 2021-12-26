from flask import Flask, render_template, request, url_for, flash, redirect
from app import app
import app.anagrams as anagrams

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        num_tiles = request.form['tiles']
        num_seconds = request.form['seconds']
        new_game = anagrams.anagrams(num_seconds, num_tiles)
        # return render_template("game.html")
    return render_template("index.html")


@app.route("/game", methods=('GET', 'POST'))
def game():
    if request.method == 'POST':
        # add to database 
        return None
    return render_template("game.html")

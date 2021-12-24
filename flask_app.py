from flask import Flask, render_template, request, url_for, flash, redirect
from game_files import anagrams

# initializes the Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '3puhljkn90W@#IT@#$MTpsdfijsfljwxczPAEsdfewi3WOE<SpaslWlksdjfj09slkdjf'

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        num_tiles = request.form['tiles']
        num_seconds = request.form['seconds']
        new_game = anagrams(num_seconds, num_tiles)
    return render_template("index.html")


@app.route("/game", methods=('GET', 'POST'))
def game():
    if request.method == 'POST':
        # add to database 
        return None
    return render_template("game.html")

# def initialize_game():

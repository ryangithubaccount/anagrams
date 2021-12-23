from flask import Flask, render_template, request, url_for, flash, redirect

# initializes the Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '3puhljkn90W@#IT@#$MTpsdfijsfljwxczPAEsdfewi3WOE<SpaslWlksdjfj09slkdjf'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

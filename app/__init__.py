from flask import Flask

# initializes the Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '3puhljkn90W@#IT@#$MTpsdfijsfljwxczPAEsdfewi3WOE<SpaslWlksdjfj09slkdjf'

from app import routes

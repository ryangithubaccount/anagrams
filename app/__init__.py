from flask import Flask
from flask_session import Session

# initializes the Flask instance
app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config['SECRET_KEY'] = '3puhljkn90W@#IT@#$MTpsdfijsfljwxczPAEsdfewi3WOE<SpaslWlksdjfj09slkdjf'
app.config.from_object(__name__)

Session(app)

from app import routes

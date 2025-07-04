from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'  # Updated to match blueprint structure

    # Import and register blueprints
    from market.routes import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app

# Import at the bottom to avoid circular imports
from market.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
from flask import Flask
from flask_migrate import Migrate
from commands import cmd
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.register_blueprint(cmd)

db.init_app(app)
migrate = Migrate(app, db)

import models

if __name__ == "__main__":
    app.run()

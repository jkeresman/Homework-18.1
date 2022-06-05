from sqla_wrapper import SQLAlchemy
import os

db_url = os.getenv("DATABASE_URL", "sqlite:///db.sqlite").replace("postgres://", "postgresql://", 1)
db = SQLAlchemy(db_url)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=False)
    last_name = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)
    message = db.Column(db.String, unique=False)


db.create_all()

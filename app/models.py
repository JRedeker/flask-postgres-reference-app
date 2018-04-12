from flask_sqlalchemy import SQLAlchemy
from app import db


# Set your classes here.
class Team(db.Model):
    __tablename__ = 'teams'

    team_id = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    players = db.relationship('Player', backref='team')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Team %r>' % self.name


class Player(db.Model):
    __tablename__ = 'players'

    player_id = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    team_id = db.Column(db.String(60))

    def __init__(self, name, team_id):
        self.name = name
        self.team_id = team_id


class Statistic(db.Model):
    __tablename__ = 'statistics'

    stat_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    position_type = db.Column(db.String(20))
    positive = db.Column(db.Boolean())

    def __init__(self, name, position_type, positive):
        self.name = name
        self.position_type = position_type
        self.positive = positive


class PlayerStat(db.Model):
    __tablename__ = 'player_stats'

    id = db.Column(db.Integer, primary_key=True)
    stat_id = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.String(60))
    career = db.Column(db.Integer)
    recent = db.Column(db.Integer)

    def __init__(self, stat_id, player_id, career, recent):
        self.stat_id = stat_id
        self.player_id = player_id
        self.career = career
        self.recent = recent


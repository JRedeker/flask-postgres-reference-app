from database.database import db


# Set your classes here.
class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    players = db.relationship('Player', backref='teams', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Team %r>' % self.name


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(30))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    def __init__(self, name, position, team_id):
        self.name = name
        self.position = position
        self.team_id = team_id


class Statistic(db.Model):
    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    stat_type = db.Column(db.String(60), nullable=False)
    position_type = db.Column(db.String(20))
    positive = db.Column(db.Boolean())

    def __init__(self, name, position_type, stat_type, positive):
        self.name = name
        self.position_type = position_type
        self.stat_type = stat_type
        self.positive = positive


class PlayerStat(db.Model):
    __tablename__ = 'player_stats'

    id = db.Column(db.Integer, primary_key=True)
    stat_id = db.Column(db.Integer, db.ForeignKey('stats.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    career = db.Column(db.DECIMAL)
    recent = db.Column(db.DECIMAL)

    def __init__(self, stat_id, player_id, career, recent):
        self.stat_id = stat_id
        self.player_id = player_id
        self.career = career
        self.recent = recent


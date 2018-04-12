from flask_sqlalchemy import SQLAlchemy

from app import *
from models import Team, Player, Statistic, PlayerStat


def mock_data():
    # insert teams
    cubs = Team("Chicago Cubs")
    yankees = Team('New York Yankees')
    tigers = Team("Detroit Tigers")
    db.session.add_all([cubs, yankees, tigers])

    db.session.flush()

    # insert players
    arizzo = Player("Anthony Rizzo", cubs.id)
    kbryant = Player("Kris Bryant", cubs.id)
    kschwarber = Player("Kyle Schwarber", cubs.id)
    jbaez = Player("Javier Baez", cubs.id)
    db.session.add_all([arizzo, kbryant, kschwarber, jbaez])

    db.session.flush()

    # insert stats
    ba = Statistic("Batting Average", "Batting", True)
    obp = Statistic("On Base Percentage", "Batting", True)
    slg = Statistic("Slugging Percentage", "Batting", True)

    db.session.add_all([ba, obp, slg])

    db.session.flush()

    # insert player stat records
    db.session.add(PlayerStat(ba.id, arizzo.id, .273, .268))
    db.session.add(PlayerStat(obp.id, arizzo.id, .366, .219))
    db.session.add(PlayerStat(slg.id, arizzo.id, .214, .485))

    db.session.add(PlayerStat(ba.id, kbryant.id, .289, .348))
    db.session.add(PlayerStat(obp.id, kbryant.id, .390, .464))
    db.session.add(PlayerStat(slg.id, kbryant.id, .530, .630))

    db.session.commit()
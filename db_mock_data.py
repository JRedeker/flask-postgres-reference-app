from dashboard.dashboard import db
from dashboard.models import *

db.drop_all()
db.create_all()

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
sp = Statistic("Slugging Percentage", "Batting", True)

db.session.add_all([ba, obp, sp])

db.session.flush()

# insert player stat records
db.session.add(PlayerStat(ba.id, arizzo.id, .300, .260))

db.session.commit()

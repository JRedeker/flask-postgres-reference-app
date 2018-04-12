from dashboard import db
from models import Team, Player

db.create_all()

# insert data
db.session.add(Team("Chicago Cubs"))
db.session.add(Player("Anthony Rizzo"))
db.session.add(Player("Kris Bryant"))


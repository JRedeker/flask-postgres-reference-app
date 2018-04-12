from dashboard.app import db
from dashboard.models import Team, Player

db.drop_all()
db.create_all()

db.session.commit()

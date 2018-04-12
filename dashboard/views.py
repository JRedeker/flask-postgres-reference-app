from flask import render_template
from flask.blueprints import Blueprint
from database import db
from models import Team, Player, Statistic, PlayerStat

views = Blueprint('views', __name__, template_folder='templates', static_folder='static')


@views.route("/")
@views.route("/index.html")
def index():
    this = Team.query.filter_by(id=1).first()
    return this.name


@views.route("/team_dashboard/<team_id>")
def team_dashboard(team_id):
    team = Team.query.filter_by(id=team_id).first()
    players = Player.query.filter_by(team_id=team_id).all()
    print(team.name)
    link_data = {
        "sub_link_title": "Team Roster",
        "sub_link_pre": "/player_dashboard/",
        "sub_links": players
    }
    return render_template('pages/team_dashboard.html',
                           title=team.name,
                           team_name=team.name,
                           link_data=link_data,
                           players=players)


@views.route("/player_dashboard/<player_id>")
def player_dashboard(player_id):
    player = Player.query.filter_by(id=player_id).first()
    player_stats = PlayerStat.query.filter_by(player_id=player_id)
    link_data = {
        "sub_link_title": "",
        "sub_link_pre": "",
        "sub_links": ""
    }
    return render_template('pages/player_dashboard.html',
                           title=player.name,
                           player=player,
                           link_data=link_data)


# error handlers
@views.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@views.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

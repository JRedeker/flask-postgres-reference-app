from flask import render_template
from flask.blueprints import Blueprint
from database.sql import get_top_ba_players, get_player_stats, get_teams, get_team_players
from database.models import Team, Player

views = Blueprint('views', __name__, template_folder='templates', static_folder='static')


@views.route("/")
@views.route("/index.html")
def index():
    teams = Team.query.order_by(Team.name).all()
    link_data = {
        "sub_link_title": "",
        "sub_link_pre": "",
        "sub_links": "",
        "top_players": get_top_ba_players(),
        "teams": get_teams()
    }
    return render_template('pages/index.html', title='Home', teams=teams, link_data=link_data)


@views.route("/team_dashboard/<team_id>")
def team_dashboard(team_id):
    team = Team.query.filter_by(id=team_id).first()
    players = get_team_players(team_id)
    link_data = {
        "sub_link_title": "{} Roster".format(team.name),
        "sub_link_pre": "/player_dashboard/",
        "sub_links": players,
        "top_players": get_top_ba_players(),
        "teams": get_teams()
    }
    return render_template('pages/team_dashboard.html', title=team.name, team_name=team.name, link_data=link_data,
                           players=players)


@views.route("/player_dashboard/<player_id>")
def player_dashboard(player_id):
    player = Player.query.filter_by(id=player_id).first()
    player_stats = get_player_stats(player_id)
    print(player_stats)
    link_data = {
        "sub_link_title": "",
        "sub_link_pre": "",
        "sub_links": "",
        "top_players": get_top_ba_players(),
        "teams": get_teams()
    }
    return render_template('pages/player_dashboard.html', title=player.name, player=player, link_data=link_data,
                           stats=player_stats)


# error handlers
@views.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@views.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

# IMPORTS

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# create the application object
app = Flask(__name__)

# configure the application
app.config.from_pyfile('configure.py')

# create the sqlalchemy object
db = SQLAlchemy(app)

# import db scheme
from dashboard import models


# CONTROLLERS
@app.route("/")
@app.route("/index.html")
def index():
    return render_template('pages/index.html', title="Home", header="Home")


@app.route("/team_dashboard/<team>")
def team_dashboard(team):
    team_name = get_team_name(team)
    players = get_players(team)
    link_data = {
        "sub_link_title": "Team Roster",
        "sub_link_pre": "/player_dashboard/",
        "sub_links": players
    }
    return render_template('pages/team_dashboard.html',
                           title=team_name,
                           team_name=team_name,
                           link_data=link_data,
                           players=players)


@app.route("/player_dashboard/<player_id>")
def player_dashboard(player_id):
    player = get_player(player_id)
    link_data = {
        "sub_link_title": "",
        "sub_link_pre": "",
        "sub_links": ""
    }
    return render_template('pages/player_dashboard.html',
                           title=player['name'],
                           player=player,
                           link_data=link_data)


# # Database test
# @dashboard.route("/dbtest")
# def database_test():

# error handlers
@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


# 🚀 LAUNCH  🚀
if __name__ == "__main__":
    app.run(host='0.0.0.0')

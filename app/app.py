# IMPORTS
import psycopg2
import yaml
import json

from flask import Flask, render_template

# APP CONFIG
app = Flask(__name__)
app.config.from_pyfile('configure.py')

config_file = open("config.yml", "r")
config = yaml.load(config_file)
db = config['database_cfg']

# data placeholder
team_data = json.load(open("team_data.json"))
player_data = json.load(open("player_data.json"))

# placeholder just deal with it


def get_team_name(team):
    this_team_name = team_data[team]['name']
    return this_team_name


def get_players(team):
    this_team_data = team_data[team]['players']
    this_team_players = {
        player_id: {
            'name': get_player_name(player_id),
            'position': get_player(player_id)['position']
        } for player_id in this_team_data
    }
    return this_team_players


def get_player(player_id):
    this_player_data = player_data[player_id]
    return this_player_data


def get_player_stats(player_id):
    this_player_stats = player_data[player_id]['stats']
    return this_player_stats


def get_player_name(player_id):
    this_player_name = player_data[player_id]['name']
    return this_player_name


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
                           title=player.name,
                           stats=player.stats,
                           link_data=link_data)


@app.route("/dbtest")
def dbtest():

    try:

        connection = psycopg2.connect(**db)
        cursor = connection.cursor()

        cursor.execute("""SELECT * FROM {}""".format(config['tables']['main']))

        connection.close()

        return "Database connected"

    except:

        return "Database not connected!"


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


# 🚀 LAUNCH  🚀


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

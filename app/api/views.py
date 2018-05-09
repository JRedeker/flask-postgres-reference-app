from flask.blueprints import Blueprint
from api.sql import *
from flask import abort

# get_top_ba_players, get_player_stats, get_teams, get_team_players

api = Blueprint('api', __name__)


@api.route('/single_player_stats/<player_id>', methods=['GET'])
def single_player_stats(player_id):
    return get_single_player_stats(player_id=player_id)

@api.route('/get_top_stat_players/<>')


# @api.route('/update_single_player_stats/<player_id>', methods=['POST'])
# def update_single_player_stats(player_id):
#     update_single_player_stats

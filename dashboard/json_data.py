import json

# data placeholder
team_data = json.load(open("team_data.json"))
player_data = json.load(open("player_data.json"))

# placeholder data and methods just deal with it


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

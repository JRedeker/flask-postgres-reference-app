from models import Team, Player, PlayerStat, Statistic


# Some logic that will be used numerous times for different views

def get_top_players_by_stat(stat_name):
    ba_stat = Statistic.query.filter_by(name=stat_name).first()
    players = Player.query.join(PlayerStat).filter_by(stat_id=ba_stat.id).order_by(PlayerStat.recent).limit(3).all()
    return players


def get_top_ba_players():
    players = get_top_players_by_stat("Batting Average")
    return players


def get_player_stats(player_id):
    player_stats = PlayerStat.query.join(Statistic).filter_by(id=player_id).all()
    return player_stats


def get_teams():
    teams = Team.query.all()
    return teams
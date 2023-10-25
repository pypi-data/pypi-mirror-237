from pgn_manager.pmanager import _readPGN

##########! DANGEROUS AREA !##########
#! This script needs testing
#! DON'T USE!
#TODO: GUI, filter_time, filter match score better
#1--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_player(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') or player in game.headers.get('Black'):
            games_filtered.append(game)
    return games_filtered

def filter_white(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White'):
            games_filtered.append(game)
    return games_filtered

def filter_black(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('Black'):
            games_filtered.append(game)
    return games_filtered
#2--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_player_win(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
            continue
        if player in game.headers.get('Black') and game.headers.get('Result') == '0-1':
            games_filtered.append(game)
    return games_filtered

def filter_player_win_white(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
    return games_filtered

def filter_player_win_black(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('Black') and game.headers.get('Result') == '0-1':
            games_filtered.append(game)
    return games_filtered
#3--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_player_lose(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '0-1':
            games_filtered.append(game)
            continue
        if player in game.headers.get('Black') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
    return games_filtered

def filter_player_lose_white(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '0-1':
            games_filtered.append(game)
    return games_filtered

def filter_player_lose_black(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('Black') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
    return games_filtered
#4--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TODO:function review necessity (don't use)
def filter_player_draws(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if (player in game.headers.get('White') or player in game.headers.get('Black')) and game.headers.get('Result') == '1/2-1/2': 
            games_filtered.append(game)
    return games_filtered

def filter_player_draw_white(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and game.headers.get('Result') == '1/2-1/2': 
            games_filtered.append(game)
    return games_filtered

def filter_player_draw_black(pgn, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('Black') and game.headers.get('Result') == '1/2-1/2': 
            games_filtered.append(game)
    return games_filtered
#5--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_for_eco(pgn, eco):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if eco == game.headers.get('ECO'):
            games_filtered.append(game)
    return games_filtered

def filter_for_white_player_eco(pgn, eco, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and eco == game.headers.get('ECO'):
            games_filtered.append(game)
    return games_filtered

def filter_for_white_player_eco_win(pgn, eco, player):
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if player in game.headers.get('White') and eco == game.headers.get('ECO') and game.headers.get('Result') == '1-0':
            games_filtered.append(game)
    return games_filtered

'''
#? def filter_for_black_player_eco(pgn, eco, player)
#? def filter_for_black_player_eco_win(pgn, eco, player)
'''
#6--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def filter_time(pgn, time): #time is a parameter not standard in PGN file. Added from Eros script
    games = _readPGN(pgn)
    games_filtered = []
    for game in games:
        if time == game.headers.get('Time'):
            games_filtered.append(game)
    return games_filtered
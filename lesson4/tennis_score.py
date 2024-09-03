from random import randrange

MAX_NUMBER_OF_PLAYERS = 2
MIN_DIFF_TO_WIN_SET_OR_MATCH = 2
MIN_NUMBER_OF_GAMES_TO_WIN_SET = 6
MAX_NUMBER_OF_SETS = 3
MIN_DIFF_TO_WIN_A_GAME = 2
MIN_NUMBER_OF_POINTS_TO_WIN_A_GAME = 4

INITIAL_SCORE = 0

FIRST_PLAYER = 0
SECOND_PLAYER = 1

match_score = [[INITIAL_SCORE, INITIAL_SCORE], [INITIAL_SCORE, INITIAL_SCORE], [INITIAL_SCORE, INITIAL_SCORE]]


def is_there_a_match_winner(score_in_match):
    first_player_score = INITIAL_SCORE
    second_player_score = INITIAL_SCORE

    for score_in_set in score_in_match:
        if not is_there_a_set_winner(score_in_set):
            continue

        if FIRST_PLAYER == get_winner(score_in_set):
            first_player_score += 1
        else:
            second_player_score += 1

        if first_player_score == MIN_DIFF_TO_WIN_SET_OR_MATCH or second_player_score == MIN_DIFF_TO_WIN_SET_OR_MATCH:
            return True

    return False


def is_there_a_set_winner(score_in_set):
    first_player_score, second_player_score = score_in_set

    if (first_player_score >= MIN_NUMBER_OF_GAMES_TO_WIN_SET
            and second_player_score <= first_player_score - MIN_DIFF_TO_WIN_SET_OR_MATCH):
        return True

    if (second_player_score >= MIN_NUMBER_OF_GAMES_TO_WIN_SET
            and first_player_score <= second_player_score - MIN_DIFF_TO_WIN_SET_OR_MATCH):
        return True

    return False


def get_winner(score):
    if score[FIRST_PLAYER] > score[SECOND_PLAYER]:
        return FIRST_PLAYER

    return SECOND_PLAYER


def play_game():
    score_in_game = [INITIAL_SCORE, INITIAL_SCORE]

    while not is_there_a_game_winner(score_in_game):
        winner = randrange(FIRST_PLAYER, SECOND_PLAYER + 1)
        score_in_game[winner] += 1

    return score_in_game


def is_there_a_game_winner(score_in_game):
    first_player_score, second_player_score = score_in_game

    if (first_player_score >= MIN_NUMBER_OF_POINTS_TO_WIN_A_GAME
            and second_player_score <= first_player_score - MIN_DIFF_TO_WIN_A_GAME):
        return True

    if (second_player_score >= MIN_NUMBER_OF_POINTS_TO_WIN_A_GAME
            and first_player_score <= second_player_score - MIN_DIFF_TO_WIN_A_GAME):
        return True

    return False


for set_number in range(len(match_score)):
    set_is_the_third = set_number == MIN_DIFF_TO_WIN_SET_OR_MATCH

    if set_is_the_third and is_there_a_match_winner(match_score):
        break

    set_score = match_score[set_number]

    while not is_there_a_set_winner(set_score):
        game_score = play_game()
        game_winner = get_winner(game_score)
        set_score[game_winner] += 1

print(match_score)

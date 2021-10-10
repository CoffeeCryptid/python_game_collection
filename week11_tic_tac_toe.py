"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    """
    a single monte carlo trial
    """
    empty = board.get_empty_squares()
    while board.check_win() is None:
        square = random.choice(empty)
        board.move(square[0], square[1], player)
        player = provided.switch_player(player)
        empty = board.get_empty_squares()
    return board

def mc_update_scores(scores, board, player):
    """
    score board after monte carlo trial
    """
    dim = board.get_dim()
    win = board.check_win()
    if win in [provided.PLAYERX, provided.PLAYERO]:
        for i_row in range(dim):
            for i_col in range(dim):
                value = board.square(i_row, i_col)
                if value == win:
                    scores[i_row][i_col] += SCORE_CURRENT
                elif value == provided.switch_player(win):
                    scores[i_row][i_col] -= SCORE_OTHER

def get_best_move(board, scores):
    """
    Determine the best possible move from a score board
    """
    empty = board.get_empty_squares()
    best = -float("inf")
    for i_row, row in enumerate(scores):
        for i_col, tile in enumerate(row):
            if tile > best and (i_row, i_col) in empty:
                best = tile
    
    best_position = []
    for i_row, row in enumerate(scores):
        for i_col, tile in enumerate(row):
            if tile == best and (i_row, i_col) in empty:
                best_position.append((i_row, i_col))

    return random.choice(best_position)

def mc_move(board, player, trials):
    """
    run monte carlo trials and determine best move
    """
    dim = board.get_dim()
    scores = [[0] * dim for dummy_i in range(dim)]
    for dummy_i in range(trials):
        trial = mc_trial(board.clone(), player)
        mc_update_scores(scores, trial, player)
    
    position = get_best_move(board, scores)
    return position
    

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

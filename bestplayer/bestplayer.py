import random
import sys
import time
import math
sys.path.append('..')
from common import board

start_time = time.time()

# Heuristica diferença de moedas:
# coin_heuristic_value = (max_coins - min_coins) / (max_coins + min_coins)

# Heuristica mobilidade: 
# if (max_moves + min_moves) != 0 then mobility_heuristic_value = (max_moves - min_moves) / (max_moves + min_moves) else mobility_heuristic_value = 0

# Heuristica cantos capturados:
# if (max_corner + min_corner) != 0 then corner_heuristic_value = (max_corner - min_corner) / (max_corner + min_corner) else corner_heuristic_value = 0

# Heuristica de estabilidade:
# if (max_stability_value + min_stability_value) != 0 then stability_heuristic_value = (max_stability_value - min_stability_value) / (max_stability_value + min_stability_value) else stability_heuristic_value = 0
alpha = 0
beta = 0


        
def heur_coins_count(state, color):    
    opp = state.piece_count[state.opponent(color)]
    my_count = state.piece_count[color]

    print("meu ",my_count)
    print("dele ",opp)

    coin_heur_value = (my_count - opp) / (opp + my_count)    

    return coin_heur_value
    

##def heur_coins_count
##def heur_coins_count
##def heur_coins_count



def minimax(state, color):
    """
    Returns a minimax move given the current state
    :param state:
    :return: (int, int)
    """
    old_state = state
    v = value_max(state, -math.inf, math.inf, color)
    print(v)
    print(heur_coins_count(old_state, color))

    for st in old_state.legal_moves(color):
        old_state.process_move(st, color)
        print(heur_coins_count(old_state, color))
        if heur_coins_count(old_state, color) == v:
            return st

    return (-1,-1)

def value_max(state, alpha, beta, color):    
    """
    Returns a supporting value given the current state and alpha and beta values
    :return:move
    """
    print(color)
    actual_time = time.time() - start_time
    
    if actual_time >= 0.9:
        print("heuristica ",heur_coins_count(state, color))
        return heur_coins_count(state, color)

    for st in state.legal_moves(color):
        state.process_move(st, color)
        v = value_min(state, alpha, beta, state.opponent(color))
        alpha = max(alpha, v)
        if beta < alpha:
            print(alpha)
            return alpha
    print(alpha)
    return alpha
    

def value_min(state, alpha, beta, color):
    """
    Returns a supporting value given the current state and alpha and beta values
    :return:move
    """
    print(color)
    actual_time = time.time() - start_time
    
    if actual_time >= 0.9:
        print("heuristica ",heur_coins_count(state, color))
        return heur_coins_count(state, color)

    for st in state.legal_moves(color):
        state.process_move(st, color)
        v = value_max(state, alpha, beta, state.opponent(color))
        beta = min(beta, v)
        if beta < alpha:
            print(beta)
            return beta
    print(beta)
    return beta

    
def make_move(the_board, color):
    """
    Returns a random move from the list of possible ones
    :return: (int, int)
    """
    color = board.Board.WHITE if color == 'white' else board.Board.BLACK
    legal_moves = the_board.legal_moves(color)

    return minimax(the_board, color) if len(legal_moves) > 0 else (-1, -1)


if __name__ == '__main__':
    b = board.from_file(sys.argv[1])
    f = open('move.txt', 'w')
    f.write('%d,%d' % make_move(b, sys.argv[2]))
    f.close()

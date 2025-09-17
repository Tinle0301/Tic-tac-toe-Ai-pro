"""
Tic Tac Toe Player

Name: Trung Tin Le
ID: 032475818

"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid move: Cell is not empty.")

    new_board = [row[:] for row in board]  
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False  
    return True  


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    ai_player = player(board)  # Who is the AI this turn (X or O)

    def evaluate(state):
        """
        Interprets utility from the AI's perspective.
        """
        score = utility(state)
        return score if ai_player == X else -score

    def max_value(state):
        if terminal(state):
            return evaluate(state)
        value = -math.inf
        for action in actions(state):
            value = max(value, min_value(result(state, action)))
        return value

    def min_value(state):
        if terminal(state):
            return evaluate(state)
        value = math.inf
        for action in actions(state):
            value = min(value, max_value(result(state, action)))
        return value

    best_move = None
    best_score = -math.inf

    for action in actions(board):
        next_state = result(board, action)
        score = min_value(next_state)
        if score > best_score:
            best_score = score
            best_move = action

    return best_move
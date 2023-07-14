import copy
import math
import random

X = "X"
O = "O"
EMPTY = None

class tictacktoe:
    """
    Tic Tac Toe Player
    """

    def __init__(self):
        """
        starting state of the board.
        """
        self.board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]


    def player(self, board):
        """
        Returns player who has the next turn on a board.
        """
        x, o = 0, 0
        for row in board:
            for item in row:
                if item == X:
                    x += 1
                elif item == O:
                    o += 1

        if x <= o:
            return X
        else:
            return O


    def actions(self, board):
        """
        Returns set of all possible actions (i, j) available on the board.
        """
        moves = set()

        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == EMPTY:
                    moves.add((i, j))

        return moves


    def result(self, board, action):
        """
        Returns the board that results from making move/action (i, j) on the board.
        """
        i, j = action[0], action[1]

        if (0 > i > 2) or (0 > i > 2):
            raise NameError("Invalid action", action)
        if board[i][j] != None:
            raise NameError("Invalid action", action)

        board_copy = copy.deepcopy(board)

        board_copy[i][j] = self.player(board_copy)
        return board_copy


    def winner(self, board):
        """
        Returns the winner of the game, if there is one.
        """
        if board[0][0] == board[1][1] == board[2][2] != None:
            return board[0][0]
        elif board[2][0] == board[1][1] == board[0][2] != None:
            return board[2][0]

        for i in range(0, 3):
            if board[i][0] == board[i][1] == board[i][2] != None:
                return board[i][0]
            elif board[0][i] == board[1][i] == board[2][i] != None:
                return board[0][i]
        return None


    def terminal(self, board=None):
        """
        Returns True if game is over, False otherwise.
        """
        if board is None:
            board = self.board

        cr, em = 0, 0
        for row in board:
            if None in row:
                cr += 1
            if row == [None, None, None]:
                em += 1
        if em == 3:
            return False
        elif cr == 0:
            return True

        if (board[0][0] == board[1][1] == board[2][2] != None) or (board[2][0] == board[1][1] == board[0][2] != None):
            return True

        for i in range(0, 3):
            if (board[i][0] == board[i][1] == board[i][2] != None) or (board[0][i] == board[1][i] == board[2][i] != None):
                return True

        return False


    def utility(self, board):
        """
        Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
        """
        w = self.winner(board)
        if w == X:
            return 1
        if w == O:
            return -1
        return 0

    def max_val(self, board, alpha, beta):
        if self.terminal(board):
            return self.utility(board)

        moves = self.actions(board)
        max_v = -math.inf

        while len(moves):
            move = moves.pop()
            v = self.min_val(self.result(board, move), alpha, beta)
            max_v = max(max_v, v)
            alpha = max(alpha, max_v)
            if alpha >= beta:
                break
        return max_v


    def min_val(self, board, alpha, beta):
        if self.terminal(board):
            return self.utility(board)

        moves = self.actions(board)
        min_v = math.inf

        while len(moves):
            move = moves.pop()
            v = self.max_val(self.result(board, move), alpha, beta)
            min_v = min(v, min_v)
            beta = min(beta, min_v)
            if alpha >= beta:
                break
        return min_v
    
    def minimax(self):
        turn = self.player(self.board)
        moves = self.actions(self.board)
        move = None
        # vals_moves = {}
        movesList = []
        vals = []
        alpha, beta = -math.inf, math.inf
        if turn == X:
            while len(moves):
                move = moves.pop()
                v = self.min_val(self.result(self.board, move), alpha, beta)
                alpha = max(v, alpha)
                vals.append(v)
                movesList.append(move)
            # return 
            move_to_make = movesList[vals.index(alpha)]
            self.board[move_to_make[0]][move_to_make[1]] = X

        else:
            while len(moves):
                move = moves.pop()
                v = self.max_val(self.result(self.board, move), alpha, beta)
                beta = min(v, beta)
                vals.append(v)
                movesList.append(move)
            # return 
            move_to_make = movesList[vals.index(beta)]
            self.board[move_to_make[0]][move_to_make[1]] = O

        
    def print_board(self, board = None):
        if board is None:
            board = self.board
        
        for row in self.board:
            print(row)
        print()
        

if __name__=='__main__':
    ttt = tictacktoe()
    while(not ttt.terminal()):
        ttt.minimax()
        ttt.print_board()

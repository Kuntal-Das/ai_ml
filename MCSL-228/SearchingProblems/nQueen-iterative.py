import copy
import numpy as np


class NQueenRecursive:
    def __init__(self,n):
        self.N = n
        self.Board = np.zeros((n, n))
        self.Solutions = list()
    
    def get_positions_for_next_queen(self, row_to_fill, n):
        if row_to_fill == n:
            return np.array([])
        return np.array([[row_to_fill, j] for j in range(0,n)], dtype= int)

    def is_move_possible(self, board, position, n):      
        left_diagonal = position[0] - position[1]
        right_diagonal = position[0] + position[1]

        for i in range(0, n):
            for j in range(0, n):
                if position[0] == i and board[i,j] != 0:
                    return False
                if position[1] == j and board[i,j] != 0:
                    return False
                
                temp_ld = i - j
                temp_rd = i + j
                if temp_ld == left_diagonal and board[i,j] != 0:
                    return False
                if temp_rd == right_diagonal and board[i,j] != 0:
                    return False
        return True
    
    def is_result_already_found(self, result):
        for solution in self.Solutions:
            if (result == solution).all():
                return True
        return False
    
    def backtrack(self, board, row, n):
        if np.sum(board) == self.N:
            return True
        
        board_copy = copy.deepcopy(board)
        next_positions = self.get_positions_for_next_queen(row, n)
        for position in next_positions:
            if self.is_move_possible(board_copy, position, n):
                board_copy[position[0],position[1]] = 1
                if self.backtrack(board_copy, row+1, n):
                    self.Solutions.append(board_copy)
                    
                board_copy[position[0],position[1]] = 0
        
        return False
    
    def print_solutions(self, print_solutions=False):
        print(f"No of solutions for N={self.N} is {len(self.Solutions)}")

        if print_solutions:
            for solution in self.Solutions:
                print(solution,end="\n\n")

    def solve(self, print_solutions=False):
        # self.backtrack(self.Board, 0, self.N)
        # self.print_solutions(print_solutions)

        Q = np.array([-1 for _ in range(self.N)])
        row_restart = 0
        went_to_row0_colN = False
        while not went_to_row0_colN and self.N > 0:
            for i in range(row_restart, self.N):
                isAssigned = False
                for j in range(Q[i]+1, self.N):
                    if i==0 and j==self.N - 1:
                        went_to_row0_colN=True
                    if self.is_move_possible(self.Board, [i,j], self.N):
                        self.Board[i,j] = 1
                        isAssigned = True
                        Q[i] = j
                        break
                if not isAssigned and Q[i]!=-1:
                    Q[i] = -1

                if i == self.N - 1 and np.sum(self.Board) == self.N:
                    self.Solutions.append(copy.deepcopy(self.Board))
            
            for row_restart in range(self.N-1, -1, -1):
                if Q[row_restart] < 0: 
                    continue
                self.Board[row_restart, Q[row_restart]] = 0
                break
              
        self.print_solutions(print_solutions)                
                    

if __name__ == '__main__':
    for n in range(0, 11):
        n_queen = NQueenRecursive(n)
        n_queen.solve()

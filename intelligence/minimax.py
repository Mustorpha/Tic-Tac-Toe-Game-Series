from math import inf as infinity

class Intelligence ():

    '''
    An Aritificial intelligence object class for finding
    the best move for a player in a tic tac toe Game.
    It uses the minimax algorithm to find the move that
    best maximises the minimum loss for every state of the game.
    '''

    def __init__(self, player, opponent):

        '''
        Intializes the class with appropiate properties
        '''

        self.player = player
        self.opponent = opponent

    def isMovesLeft(self, board) :
        
        '''
        Return False if the game board is full and
        True otherwise
        '''

        for i in range(3) :
            for j in range(3) :
                if (board[i][j] == ' ') :
                    return True
        return False

    def evaluate(self, b) :

        '''
        Check if a player won the game for a particular
        state of the board and return a value which is 
        known as the value of the game at that state
        '''

        # Checking for Rows for X or O victory.
        for row in range(3) :	
            if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :	
                if (b[row][0] == self.player) :
                    return 10
                elif (b[row][0] == self.opponent) :
                    return -10

        # Checking for Columns for X or O victory.
        for col in range(3) :
        
            if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
            
                if (b[0][col] == self.player) :
                    return 10
                elif (b[0][col] == self.opponent) :
                    return -10

        # Checking for Diagonals for X or O victory.
        if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
        
            if (b[0][0] == self.player) :
                return 10
            elif (b[0][0] == self.opponent) :
                return -10

        if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
        
            if (b[0][2] == self.player) :
                return 10
            elif (b[0][2] == self.opponent) :
                return -10

        # Else if none of them have won then return 0
        return 0

    def minimax(self, board, depth, isMax, alpha = -infinity, beta = infinity) :

        '''
        This is the minimax function. It considers all
        the possible ways the game can go and returns
        the value of the game for each route
        '''
        score = Intelligence.evaluate(self, board)

        # If Maximizer has won the game return it's evaluated score
        if (score == 10) :
            return score - depth    # go for the fastest winning route

        # If Minimizer has won the game return it's evaluated score
        if (score == -10) :
            return score + depth    # go for the slowest losing route

        # If there are no more moves and no winner then it is a tie
        if (Intelligence.isMovesLeft(self, board) == False) :
            return 0

        # If this is maximizer's move
        if (isMax) :	
            best = -infinity

            # Traverse all cells
            for i in range(3) :		
                for j in range(3) :
                
                    # Check if cell is empty
                    if (board[i][j]==' ') :
                    
                        # Make the move
                        board[i][j] = Intelligence.player

                        # Call minimax recursively and choose the maximum value
                        best = max( best, Intelligence.minimax(self, board,
                                                depth + 1,
                                                False, alpha, beta) )
                        alpha = max(alpha, best)
                        # Undo the move
                        board[i][j] = ' '
                        if beta <= alpha:
                            break
            return best

        # If this minimizer's move
        else :
            best = infinity

            # Traverse all cells
            for i in range(3) :		
                for j in range(3) :
                
                    # Check if cell is empty
                    if (board[i][j] == ' ') :
                    
                        # Make the move
                        board[i][j] = Intelligence.opponent

                        # Call minimax recursively and choose the minimum value
                        best = min(best, Intelligence.minimax(board, depth + 1, True, alpha, beta))
                        beta=min(beta,best)
                        # Undo the move
                        board[i][j] = ' '
                        if beta <= alpha:
                            break

            return best

    # Decide the next move of computer
    def findBestMove(board) : 
        bestVal = -infinity
        bestMove = (-1, -1)

        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3) :	
            for j in range(3) :
            
                # Check if cell is empty
                if (board[i][j] == ' ') :
                
                    # Make the move
                    board[i][j] = Intelligence.player

                    # compute evaluation function for this
                    # move.
                    moveVal = Intelligence.minimax(board, 0, False)

                    # Undo the move
                    board[i][j] = ' '

                    # If the value of the current move is
                    # more than the best value, then update
                    # best value
                    if (moveVal > bestVal) :			
                        bestMove = (i, j)
                        bestVal = moveVal

        print("The value of the best Move is :", bestVal)
        print(bestMove)
        return bestMove

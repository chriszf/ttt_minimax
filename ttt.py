class Board(object):
    def __init__(self):
        self.spaces = [" "] * 9

    def play(self, position, piece):
        if self.spaces['position'] != ' ':
            return None
        self.spaces[position] = piece

    def all(self, pos):
        (pos1, pos2, pos3) = pos
        marker = self.spaces[pos1]
        if self.spaces[pos2] == self.spaces[pos3] and self.spaces[pos2] == marker and marker != " ":
            return marker
        return None
        
    def winner(self):
        winner = self.all((0, 1, 2)) or self.all((3, 4, 5)) or self.all((6, 7, 8)) or \
                 self.all((0, 3, 6)) or self.all((1, 4, 7)) or self.all((2, 5, 8)) or \
                 self.all((0, 4, 8)) or self.all((6, 4, 2))

        if winner:
            return winner

        if len(self.empty()):
            return None
        else:
            return 0

    def __str__(self):
        top = "|".join(self.spaces[:3])
        mid = "|".join(self.spaces[3:6])
        bot = "|".join(self.spaces[6:])
        sep = "-+-+-"
        return "\n".join([top, sep, mid, sep, bot])

    def empty(self):
        return [ i for i in range(len(self.spaces)) if self.spaces[i] == " " ]

    def copy(self):
        c = Board()
        c.spaces = list(self.spaces)
        return c


class AI(object):
    nextmarker = {"X": "O", "O": "X"}
    def __init__(self, marker, board):
        self.marker = marker
        self.board = board

    def play(self):
        if len(self.board.empty()) == 9:
            self.board.play(0, self.marker)
            print self.board
            return
        next_moves = self.generate_successors(self.board, self.marker)
        scores = [ (self.minimax(b, self.marker), pos) for b, pos in next_moves ]
        # scores = [ (score, pos) ]
        self.board.play(sorted(scores)[-1][1], self.marker)
        print self.board
    
    def minimax(self, board, marker):
        winner = board.winner()
        if winner == 0:
            return 0
        elif winner == self.marker:
            return 1
        elif winner != None:
            return -1

        marker = AI.nextmarker[marker]
        children = self.generate_successors(board, marker) 

        if marker == self.marker:
            return max([ self.minimax(b, marker) for b, pos in children ]) 
        else:
            return min([ self.minimax(b, marker) for b, pos in children ])


    def generate_successors(self, board, marker):
        empties = board.empty()
        boards = []
        for pos in empties:
            new_b = board.copy()
            new_b.play(pos, marker)
            boards.append((new_b, pos))

        return boards

b = Board()
ai = AI("O", b)
ai.play()
ai2 = AI("X", b)


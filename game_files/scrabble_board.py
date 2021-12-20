class scrabble_board:
    def __init__(self):
        self.board = {}
        self.board_status = {}
        for i in range(-7, 8):
            for j in range(-7, 8):
                self.board[(i, j)] = "__"
                self.board_status[(i, j)] = False
        self.populate_dl()
        self.populate_tl()
        self.populate_dw()
        self.populate_tw()
        self.available = []
        self.taken = []

    def populate_ring(self, a, b, val):
        for i in (-a, a):
            for j in (-b, b):
                self.board[(i, j)] = val
                self.board[(j, i)] = val

    def populate_dl(self):
        self.populate_ring(7, 4, "dl")
        self.populate_ring(5, 1, "dl")
        self.populate_ring(4, 4, "dl")
        self.populate_ring(1, 1, "dl")
    
    def populate_tl(self):
        self.populate_ring(6, 2, "tl")
        self.populate_ring(2, 2, "tl")
    
    def populate_dw(self):
        for i in range(3, 7):
            self.populate_ring(i, i, "dw")
    
    def populate_tw(self):
        self.populate_ring(7, 0, "tw")
        self.populate_ring(7, 7, "tw")
    
    def get(self, i, j):
        return self.board[(i, j)]

    def set(self, i, j, val):
        #add error later
        self.board_status[(i, j)] = True
        self.taken.append((i, j))
        self.board[(i, j)] = val

    def add_letters(self, i, j, direction, tiles):
        #tiles are in order
        #direction: 1 is left to right, 0 is up and down
        if len(self.taken) == 0:
            if direction:
                self.available.append((i - 1, j))
                self.available.append((i + len(tiles), j))
                for num in range(len(tiles)):
                    self.set(i + num, j, tiles[num] + ' ')
                    self.available.append((i + num, j + 1))
                    self.available.append((i + num, j - 1))
            else:
                self.available.append((i, j + 1))
                self.available.append((i, j - len(tiles)))
                for num in range(len(tiles)):
                    self.set(i, j - num, tiles[num] + ' ')
                    self.available.append((i + 1, j - num))
                    self.available.append((i - 1, j - num))
        else:
            if direction:
                for num in range(len(tiles)):
                    self.set(i + num, j, tiles[num] + ' ')
                    try:
                        self.available.remove((i + num, j))
                    except ValueError:
                        pass
                    if j + 1 < 8 and (i + num, j + 1) not in self.taken:
                        self.available.append((i + num, j + 1))
                    if j - 1 > -8 and (i + num, j - 1) not in self.taken:
                        self.available.append((i + num, j - 1))
                if i + len(tiles) < 8 and (i + len(tiles), j) not in self.taken:
                    self.available.append((i + len(tiles), j))
                if i - 1 > -8 and (i - 1, j) not in self.taken:
                    self.available.append((i - 1, j))

            else:
                for num in range(len(tiles)):
                    self.set(i, j - num, tiles[num] + ' ')
                    try:
                        self.available.remove((i, j - num))
                    except ValueError:
                        pass
                    if i + 1 < 8 and (i + 1, j - num) not in self.taken:
                        self.available.append((i + 1, j - num))
                    if i - 1 > -8 and (i - 1, j - num) not in self.taken:
                        self.available.append((i - 1, j - num))
                if j - len(tiles) > -8 and (i, j - len(tiles)) not in self.taken:
                    self.available.append((i, j - len(tiles)))
                if j + 1 > -8 and (i, j + 1) not in self.taken:
                    self.available.append((i, j + 1))


    def get_available_spots(self):
        if len(self.taken) == 0:
            return None
        return self.available

    def calculate_border(self, i, j, direction):
        #direction: (x, y)
        length = 0
        plus_minus = 1
        remainder = ''
        for num in range(7):
            i += direction[0]
            j += direction[1]
            if i > 7 or i < -7 or j > 7 or j < -7:
                length = num + 1
                break
            
            if self.board_status[(i, j)]:
                length = num + 1
                while ((i > 8 and i < -8 and j > 8 and j < -8) and self.board_status[i, j]):
                    remainder += self.board[(i, j)]
                    i += direction[0]
                    j += direction[1]
                break
            
        return (length, remainder)
        

    def print_board(self):
        for i in range(-7, 8):
            row = []
            for j in range(-7, 8):
                row.append(self.board[(j, -i)])
            print(row)
        
    def show_spot(self, i, j):
        val = self.board[(i, j)]
        self.board[(i, j)] = '**'
        self.print_board()
        self.board[(i, j)] = val
    
    
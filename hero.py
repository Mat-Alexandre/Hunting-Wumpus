class Hero:
    def __init__(self, perception):
        self.position = 0
        self.alive = True
        self.arrow = True
        self.safe_to_leave = False
        self.perception = perception
    
    def ask(self, world):
        for sq in world.squares:
            if sq.__str__() == self.position:
                sq.visited = True
                room = sq
        
        for sq in self.perception.squares:
            if sq.__str__() == room.__str__():
                if room.prop['Breeze'] == True:
                    print('Breeze true')
                    self.perception.squares[room.__str__()].setProperties('Breeze', True)
                    self.perception.squares[room.__str__()].setProperties('Hole', False)
                    
                    # At least one of the neighbors should have a hole
                    for nb in sq.nbh:
                        if self.perception.squares[nb.__str__()] == None:
                            self.perception.squares[nb.__str__()].setProperties('Hole', 'Maybe')
                else:
                    print('Breeze false')
                    # Call __tell function to predict where are the holes
                    self.__tell()
               
        for sq in self.perception.squares:
            print(sq.__repr__(), sq.prop)

    def __tell(self):
        print('tell function')

    def walk(self, world):
        s = self.perception.squares[self.position]
        F = []
        F.append(s)
        while len(F) != 0:
            v = F.pop(0)
            for w in v.nbh:
                if w.visited == False:
                    w.visited = True
                    print('Visit', w.id)
                    return w
                elif F.count(w):
                    print(w.id,'was visited before')
                    return w


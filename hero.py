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
                room = sq
        
        for sq in self.perception.squares:
            if sq.__str__() == room.__str__():
                if room.prop['Breeze'] == True:
                    print('Breeze true')
                    print('Hole probabily in',sq.nbh)
                else:
                    print('Breeze false')
                    print('No hole in',sq.nbh)
                
                if room.prop['Stink'] == True:
                    print('Stink true')
                    print('Wumpus probabily in',sq.nbh)
                else:
                    print('Stink false')
                    print('No wumpus in',sq.nbh)

    def __tell(self):
        print('tell function')

    def walk(self, world):
        print('shorter path to an empty room.')
import random

class Square:
    def __init__(self, id, perception):
        self.id = id
        self.nbh = []
        if perception == False:
            self.prop = {'Breeze': False, 'Hole': False, 'Wumpus': False, 'Stink': False, 'Gold': False}
        else:
            self.prop = {'Breeze': None, 'Hole': None, 'Wumpus': None, 'Stink': None, 'Gold': None}
    
    def __repr__(self):
        return '{}'.format(int(self.id))
    
    def __str__(self):
        return int(self.id)
    
    def getInfo(self):
        return 'ID:{:2},\tNeighbors:{},\t\tProperties:{}'.format(self.id, self.nbh, self.prop)
    
    def setProperties(self, key, value):
        self.prop.update({key: value})
    
class World:
    def __init__(self, perception):
        self.squares = []
        for i in range(16):
            self.squares.append(Square(i, perception))
        
        if perception == False:   
            self.__sortProperties()
        
        self.__setNeighbors()        
    
    def __neighbourhood(self, sq1, sq2):
        if 0 > sq1.__str__() % 4:
            if sq1.__str__() - 1 ==  sq2.__str__():
                return True
        if sq1.__str__() % 4 < 3 :
            if sq1.__str__() + 1 ==  sq2.__str__():
                return True
        if sq1.__str__() - 4 ==  sq2.__str__():
            return True
        elif sq1.__str__() + 4 ==  sq2.__str__():
            return True
        return False

    def __setNeighbors(self):
        for sq1 in self.squares:
            for sq2 in self.squares:
                if self.__neighbourhood(sq1, sq2) == True:
                    if sq1.nbh.count(sq2) == 0:
                        sq1.nbh.append(sq2)
                    if sq2.nbh.count(sq1) == 0:
                        sq2.nbh.append(sq1)
    
    def __setNbhProperties(self, square, key):
        for sq in self.squares[self.squares.index(square)].nbh:
            if key == 'Hole':
                sq.setProperties('Breeze', True)
            if key == 'Wumpus':
                sq.setProperties('Stink', True)

    def __sortProperties(self):
        population = [2, 3, 5, 6, 7, 8, 9, 10,11,12,13,14,15]
        weights    = [20,20,20,20,20,20,20,20,20,20,20,20,20]

        # Setting holes
        number_of_holes = random.randint(1, 3)
        holes = random.choices(population, weights, k=number_of_holes)
        for position in holes:
            for square in self.squares:
                if position == square.__str__():
                    square.setProperties('Hole', True)
                    self.__setNbhProperties(square, 'Hole')
        
        # Setting wumpus    
        wumpus = random.choices(population, weights, k=1).pop()
        for square in self.squares:
            if wumpus == square.__str__():
                square.setProperties('Wumpus', True)
                self.__setNbhProperties(square, 'Wumpus')

        # Setting gold
        gold = random.choices(population, weights, k=1).pop()
        for square in self.squares:
            if gold == square.__str__():
                square.setProperties('Gold', True)
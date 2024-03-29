import pygame
class View:
    def __init__(self):
        self.squares = []
        size = (100, 100)
        for i in range(4):
            self.squares.append([])
            for j in range(4):
                self.squares[i].append([])
        
        for i in range(4):
            for j in range(4):
                self.squares[i][j] = pygame.Rect((j*100, (3-i)*100), size)

    def heroLocation(self, hero):
        for i in range(4):
            for j in range(4):
                if 4*(3-i)+j == hero.position:
                    x = j
                    y = i
        return x, y
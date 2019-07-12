import world as wd
import hero
import pygame
import view

# sizes
padding = 5
size = (960, 540)

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

if __name__ == '__main__':
    # w = wd.World(False)
    # h.ask(w)
    p = wd.World(True)
    h = hero.Hero(p)

    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Hunting Wumpus')
    
    v = view.View()
    x = 0

    v.mapChar(h)
    
    while True:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # drawing world
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(screen, green, v.squares[i][j], 1)
        
        # drawing circle
        # pygame.draw.circle(screen, white, )
        pygame.display.flip()


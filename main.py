import world as wd
import hero
import pygame
import view as v

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
    w = wd.World(False)
    p = wd.World(True)
    h = hero.Hero(p)
    h.walk(w)

    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Hunting Wumpus')
    
    view = v.View()

    view.heroLocation(h)
    
    while True:
        screen.fill(black)
        
        # Drawing world
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(screen, green, view.squares[i][j], 1)
        
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # Keys for test
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    h.position += 4
                if event.key == pygame.K_DOWN:
                    h.position -= 4
                if event.key == pygame.K_LEFT:
                    h.position -= 1
                if event.key == pygame.K_RIGHT:
                    h.position += 1
        
        # Drawing hero
        x, y = view.heroLocation(h)
        pygame.draw.circle(screen, white, (int(x*100)+50, int(y*100)+50), 20)
        
        pygame.display.flip()

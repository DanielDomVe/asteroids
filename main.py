import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    t = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    run = True
    while run == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(000)
        player.draw(screen) 
        pygame.display.flip()
        dt = t.tick(60)/1000




if __name__ == "__main__":
    main()
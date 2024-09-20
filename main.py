import pygame # type: ignore
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


# ------------------ GAME LOOP -----------------------
    while True:

        # event handling (quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # game logic

        player.update(dt)


        # rendering
        screen.fill(000)
        player.draw(screen) 
        pygame.display.flip()

        # 60 FPS limit
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
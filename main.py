import pygame # type: ignore
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    
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

        for object in updatable:
            object.update(dt)


        # rendering
        screen.fill(000)
        
        for object in drawable:
            object.draw(screen) 
        
        pygame.display.flip()

        # 60 FPS limit
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
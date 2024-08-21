import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField
from shot import Shot

def main():
    # init pygame and create the screen object
    pygame.init()
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set FPS
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # Print out game info before launch
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"Number of drawable objects: {len(drawable)}")
    print(f"Number of updatable objects: {len(updatable)}")
    print(f"Number of asteroid objects: {len(asteroids)}")

    
    # Create the infinite game loop, launching the game
    while True:
        # Make sure the close window closes the game!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        for object in updatable:
            object.update(dt)
            for asteroid in asteroids:
                if asteroid.is_colliding(player):
                    print("Game Over!")
                    pygame.quit()
                    return
                for shot in shots:
                    if shot.is_colliding(asteroid):
                        asteroid.split()
                        shot.kill()
        
        for object in drawable:
            object.draw(screen)
            
        pygame.display.flip()
        
        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

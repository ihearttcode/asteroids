import pygame
from constants import *

def main():
    # init pygame and create the screen object
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Print out game info before launch
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Create the infinite game loop, launching the game
    while True:
        screen.fill("black")
        pygame.display.flip()
        # Make sure the close window closes the game!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()

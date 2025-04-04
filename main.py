import pygame
from constants import *
from player import Player

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    dt = 0
    pygame.time.Clock()
    while True:
        pygame.Surface.fill(screen,"black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = pygame.time.Clock().tick(60)/1000
if __name__ == "__main__":
    main()
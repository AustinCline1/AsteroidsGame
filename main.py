import pygame

from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Create groups for better control
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Adding the Player Class to these Groups
    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable, asteroids
    AsteroidField.containers = updatable
    Shot.containers = drawable,updatable,shots
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #Creating a new Player Class
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    #create a new asteroid field class
    asteroid_field = AsteroidField()
    dt = 0
    pygame.time.Clock()
    while True:
        pygame.Surface.fill(screen,"black")
        updatable.update(dt)
        for entity in asteroids:
            if entity.collision(player):
                print("Game Over!")
                return
            for shot in shots:
                if shot.collision(entity):
                    entity.split()
                    shot.kill()
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = pygame.time.Clock().tick(60)/1000
if __name__ == "__main__":
    main()
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Shot.containers = (drawable, updateable, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for object in updateable:
            object.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!!")
                return
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()

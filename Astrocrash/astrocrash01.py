#Astrocrash01
#get asteroids moving on the screen

import random
from superwires import games
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Asteroid(games.Sprite):
    #an asteroid which floats across the screen
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL : games.load_image("asteroid_small.bmp"), MEDIUM : games.load_image("asteroid_med.bmp"), LARGE : games.load_image("asteroid_big.bmp") }

    SPEED = 2

    def __init__(self, x, y, size):
        #initialize asteroid sprite
        super(Asteroid,self).__init__(image = Asteroid.images[size], x = x, y = y, dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size, dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)

        self.size = size
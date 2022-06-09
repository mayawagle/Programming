#Astrocrash
#get asteroids moving on the screen

import math,random
from turtle import update
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

    def update(self):
        #wrap around screen
        if self.top > games.screen.height:
            self.bottom = 0
        
        if self.bottom < 0:
            self.top = games.screen.height
        
        if self.left > games.screen.width:
            self.right = 0
        
        if self.right < 0:
            self.left = games.screen.width

class Ship(games.Sprite):
    #The player's ship
    image = games.load_image("ship.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = 0.03
    sound = games.load_sound("thrust.wav")

    def update(self):
        #rotate based on keys pressed
        if games.keyboard.is_pressed(games.K_LEFT):
         self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
         self.angle += Ship.ROTATION_STEP

        #apple thrust based on up arrow key
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            #change velocity components based on ship's angle
            angle = self.angle * math.pi / 180 #convert to radians
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        #wrap the ship around the screen
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width



def main():
    #establish background
    nebula_image = games.load_image("nebula.jpg")
    games.screen.background = nebula_image

    #create 8 asteroids
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x = x, y = y, size = size)
        games.screen.add(new_asteroid)
    
    #create the ship
    the_ship = Ship(image = Ship.image, x = games.screen.width/2, y = games.screen.height/2)
    games.screen.add(the_ship)

    games.screen.mainloop()


#start the game
main()
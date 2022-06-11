#Astrocrash
#get asteroids moving on the screen

import math,random
from turtle import update
from superwires import games
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Wrapper(games.Sprite):
    #a sprite that wraps around the screen
    def update(self):
        #wrap sprite around screen
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width
    
    def die(self):
        #destroy self
        self.destroy()

class Collider(Wrapper):
    #a wrapper that can collide with other objects
    def update(self):
        #check for overlapping sprites
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

class Asteroid(Wrapper):
    #an asteroid which floats across the screen
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    SPEED = 2
    SPAWN = 2
    images = {SMALL : games.load_image("asteroid_small.bmp"), MEDIUM : games.load_image("asteroid_med.bmp"), LARGE : games.load_image("asteroid_big.bmp") }

    def __init__(self, x, y, size):
        #initialize asteroid sprite
        super(Asteroid,self).__init__(
            image = Asteroid.images[size],
            x = x, y = y, 
            dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size, 
            dy = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size)
        self.size = size
    
    def die(self):
        #destroy asteroid

        #if asteroid isnt small, replace with two smaller asteroids
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(x = self.x, y = self.y, size = self.size - 1)
                games.screen.add(new_asteroid)
        super(Asteroid,self).die() 

class Ship(Collider):
    #The player's ship
    image = games.load_image("ship.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = 0.03
    MISSILE_DELAY = 25
    sound = games.load_sound("thrust.wav")

    def __init__(self, x, y):
        #initialize ship sprite
        super(Ship, self).__init__(image = Ship.image, x = x, y =y )
        self.missile_wait = 0


    def update(self):
        super(Ship, self).update()
        #rotate based on keys pressed
        if games.keyboard.is_pressed(games.K_LEFT):
         self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
         self.angle += Ship.ROTATION_STEP

        #apply thrust based on up arrow key
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            #change velocity components based on ship's angle
            angle = self.angle * math.pi / 180 #convert to radians
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        #if waiting until the ship can fire next, decrease wait
        if self.missile_wait > 0:
            self.missile_wait -= 1

        #fire missile if spacebar pressed and missile wait is over
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY
    
class Missile(Collider):
     #a missile launched by the player's ship
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        #initialize missile sprite
         Missile.sound.play()

         #convert to radians
         angle = ship_angle * math.pi / 180

         #calculate the missile's starting position
         buffer_x = Missile.BUFFER * math.sin(angle)
         buffer_y = Missile.BUFFER * -math.cos(angle)
         x = ship_x + buffer_x
         y = ship_y + buffer_y
         
         #calculate the missile's velocity components
         dx = Missile.VELOCITY_FACTOR * math.sin(angle)
         dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

         #create the missile
         super(Missile, self).__init__(image = Missile.image, x = x,
         y = y, dx = dx, dy = dy)
        
         self.lifetime = Missile.LIFETIME
    
    def update(self):
        super(Missile,self).update()
        #move the missile 
        #if lifetime is up, destroy the missile
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()
            
class Explosion(games.Animation):
    #explosion animation
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp","explosion2.bmp","explosion3.bmp",
    "explosion4.bmp","explosion5.bmp","explosion6.bmp"
    "explosion7.bmp","explosion8.bmp","explosion9.bmp"]

    def __init__(self,x,y):
        super(Explosion, self).__init__(images = Explosion.images, x = x,
        y = y, repeat_interval = 4, n_repeats = 1, is_colliadeable = False)
        Explosion.sound.play()

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
    the_ship = Ship( x = games.screen.width/2, y = games.screen.height/2)
    games.screen.add(the_ship)

    games.screen.mainloop()


#start the game
main()

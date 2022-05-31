#program of the final game starting on pg 352

#pizza panic
#player must catch falling pizzas before they hit the ground
from superwires import games, color
import random
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    #a pan controlled by the player to catch falling pizzas
    image = games.load_image('pan.bmp')

    def __init_(self):
        #initialize pan object and create text object for score
        super(Pan,self).__init__(image = Pan.image, x = games.mouse.x, bottom = games.screen.height )

        self.score = games.Text(value = 0, size = 25, color = color.black, top = 5, right = games.screen.width-10)
        games.screen.add(self.score)
    
    def update(self):
        #move to mouse x position
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0
        
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()
    
    def check_catch(self):
        #check if catch pizzas
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()


class Pizza(games.Sprite):
    #a pizza which falls to the gorund
    image = games.load_image('pizza.bmp')
    speed = 1

    def __init__(self, x, y = 90, speed = 1):
        #initialize a pizza object
        self.speed = speed
        super(Pizza, self).__init__(image = Pizza.image, x=x, y=y, dy = Pizza.speed)

    def update(self):
        #check if bottom edge has reached screen bottom
           if self.bottom > games.screen.height:
               self.end_game()
               self.destroy()
    
    def handle_caught(self):
        #destroy self if caught
        self.destroy()

    def end_game(self):
        #end the game
        end_message = games.Message(value = 'Game Over', size = 90, color=color.red, x = games.screen.width/2, y = games.screen.height/2,lifetime = 5 * games.screen.fps, after_death = games.screen.quit )
        games.screen.add(end_message)


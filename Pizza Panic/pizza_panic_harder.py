#pizza panic game but harder
#excercise 1 ch 11

#program of the final game starting on pg 352

#pizza panic
#player must catch falling pizzas before they hit the ground
from superwires import games, color
import random
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    #a pan controlled by the player to catch falling pizzas
    image = games.load_image('pan.bmp')

    def __init__(self):
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
        super(Pizza, self).__init__(image = Pizza.image, x=x, y=y, dy = self.speed)

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

class Chef(games.Sprite):
    #a chef which moves left and right, dropping pizzas
    image = games.load_image('chef.bmp')
    def __init__(self, y = 55, speed = 2, odds_change = 200):
        #initialize the chef object
        super(Chef,self).__init__(image = Chef.image, x = games.screen.width / 2, y = y, dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0
        self.index = 0
    def update(self):
        #determine if the direction needs to be reversed
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        
        self.check_drop()

    def check_drop(self):
        #decrease countdown or drop pizza and reset countdown
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x, speed = 1 + self.index)
            games.screen.add(new_pizza)

            #set buffer to approx 30% of pizza height, regardless of pizza speed
            #self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) +1
            self.time_til_drop = 100
            self.index += .1
def main():
    #play the game
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    the_chef = Chef()
    games.screen.add(the_chef)

    the_pan = Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()

#START THE GAME YAYAYAYAYAYAY
main()

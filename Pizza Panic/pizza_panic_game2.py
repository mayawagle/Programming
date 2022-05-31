#Adding code for DISPLAYING A MESSAGE pg 340

#New Graphics Window
#Demonstrates creating a graphics window

from superwires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

#Background Image
#Demonstrates setting the background image of a graphics screen
wall_image = games.load_image('wall.jpg', transparent = False)
games.screen.background = wall_image

# #Big Score
# #Demonstrates displaying text on a graphics screen
# score = games.Text(value = 123, size = 60, color = color.black, x = 550, y = 30)
# games.screen.add(score)

# #Pizza Sprite
# #demonstrates creating a sprite
# pizza_image = games.load_image('pizza.bmp')
# pizza = games.Sprite(image = pizza_image, x = 320, y = 240)
# games.screen.add(pizza)

#You Won
#Demonstrates displaying a message

won_message = games.Message(value = 'You Won!', size=100, color=color.red, x = games.screen.width/2, y = games.screen.height/2, lifetime= 250, after_death= games.screen.quit)

games.screen.add(won_message)

games.screen.mainloop()
# Pizza Panic
# Player must catch falling pizzas before they hit the ground

from livewires import games, color
import random, time, pygame
import tkinter as tk

games.init(screen_width = 640, screen_height = 480, fps = 60)


class SmallSprite(games.Sprite):
        #Initialize class variables
        image = games.load_image("images/smallSprite.png")

        def __init__(self):
                super(SmallSprite, self).__init__(image = SmallSprite.image, x = games.mouse.x,y = games.mouse.y)

        def update(self):
                self.x = games.mouse.x
                self.y = games.mouse.y 

class Card(games.Sprite):
        #Load in images, create class variables
        blocker_image = games.load_image("images/blocker.png")
        bird_image = games.load_image("images/bird.png")
        elephant_image = games.load_image("images/elephant.png")
        spider_image = games.load_image("images/spider.png")
        grape_image = games.load_image("images/grapes.png")
        peach_image = games.load_image("images/peach.png")
        pears_image = games.load_image("images/pears.png")
        cheetah_image = games.load_image("images/cheetah.png")
        chicken_image = games.load_image("images/chicken.png")
        eagle_image = games.load_image("images/eagle.png")
        guido_image = games.load_image("images/guido.png")
        lion_image = games.load_image("images/lion.png")
        tiger_image = games.load_image("images/tiger.png")
        
        cardsShowing = 0
        time = 0
        clickedCards = []
        clickable = True
        
        def __init__(self,world,x,y,whichImage = 1):
                super(Card,self).__init__(image = Card.blocker_image, x=x,y=y)

                #create instance variables for future use
                self.world = world
                self.whichImage = whichImage

        def update(self):
                """if no more than 2 cards are showing,
                   and the left mouse button is clicked,
                   figure out what image it is, replace
                   the back of the card with the image
                """
                if Card.clickable:
                        for sprite in self.overlapping_sprites:
                                for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                if event.button == 1:
                                                        if self.whichImage == 1:
                                                                self.image = Card.bird_image
                                                        elif self.whichImage == 2:
                                                                self.image = Card.elephant_image
                                                        elif self.whichImage == 3:
                                                                self.image = Card.spider_image
                                                        elif self.whichImage == 4:
                                                                self.image = Card.grape_image
                                                        elif self.whichImage == 5:
                                                                self.image = Card.peach_image
                                                        elif self.whichImage == 6:
                                                                self.image = Card.pears_image
                                                        elif self.whichImage == 7:
                                                                self.image = Card.cheetah_image
                                                        elif self.whichImage == 8:
                                                                self.image = Card.chicken_image
                                                        elif self.whichImage == 9:
                                                                self.image = Card.eagle_image
                                                        elif self.whichImage == 10:
                                                                self.image = Card.guido_image
                                                        elif self.whichImage == 11:
                                                                self.image = Card.lion_image
                                                        elif self.whichImage == 12:
                                                                self.image = Card.tiger_image
                                                        
                                                        Card.cardsShowing += 1
                                                        Card.clickedCards.append(self)
                """
                 if two cards are showing, make it so the
                 user can't click anymore cards. Calculate
                 time that the user sees both cards before
                 either destroying them, or putting them
                 back to the back of the card image.
                """
                if Card.cardsShowing == 2:
                        Card.clickable = False
                        Card.time += 1
                        if Card.time == games.screen.fps * 8:
                                for card in Card.clickedCards:
                                        if Card.clickedCards[0].whichImage == Card.clickedCards[1].whichImage:
                                                card.destroy()
                                                self.world.score.value += 5
                                                self.world.totalCards -= 1
                                                
                                                if self.world.totalCards == 0:
                                                        level_message = games.Message(value = "Level " + str(self.world.level+1),
                                                                        size = 40,
                                                                        color = color.yellow,
                                                                        x = games.screen.width/2,
                                                                        y = games.screen.width/10,
                                                                        lifetime = 5 * games.screen.fps,
                                                                        after_death = self.nextLevel,
                                                                        is_collideable = False)
                                                        games.screen.add(level_message)
                                
                                        else:
                                                Card.clickedCards[0].image = Card.blocker_image
                                                Card.clickedCards[1].image = Card.blocker_image

                                Card.time = 0
                                Card.clickedCards = []
                                Card.cardsShowing = 0
                                Card.clickable = True

        def nextLevel(self):
                Card.time = 0
                Card.clickedCards = []
                Card.cardsShowing = 0
                Card.clickable = True
                
                if self.world.level == 0:
                        self.world.level += 2

                """
                TAKE LEVEL MESSAGE OUT OF FUNCTION

                """
                        


                if World.level < World.max_rows:
                        World.rows += 1

                world = World()
                World.totalCards = World.rows * World.cols
                World.level += 1
                World.cards = []
                world.createBoard()

class World(object):
        #Initialize class variables
        cards = []
        allCards = []
        rows = 1
        cols = 6
        totalCards = rows * cols
        level = 1
        max_rows = 5

        score = games.Text(value = 0,
                                size = 30,
                                color = color.green,
                                top = 5,
                                right = games.screen.width - 25,
                                is_collideable = False)
        games.screen.add(score)

        """
         fill up the card array based on the total
         amount of cards, shuffle it, reassign it
         to the class variable named cards
        """
        def fillCardArray(self):
                """

                
                if World.level == 1:
                        for i in range(1,World.totalCards//2+1):
                                World.cards.append(i)
                                World.cards.append(i)
                        random.shuffle(World.cards)
                else:
                        for i in range(World.rows):
                                tempList = []
                                for j in range(1,World.cols+1):
                                        tempList.append(j)
                                        if j % World.cols == 0:
                                                random.shuffle(tempList)
                                                World.cards.append(tempList)
                print(World.cards)  """

                
                #testing new method
                if World.level == 1:
                        for i in range(1,World.totalCards//2+1):
                                World.cards.append(i)
                                World.cards.append(i)
                        random.shuffle(World.cards)
                else:
                        World.allCards = []
                        for i in range(1,World.totalCards//2+1):
                                World.allCards.append(i)
                                World.allCards.append(i)

                        ct = 0
                        for i in range(World.rows):
                                tempList = []
                                for j in range(1,World.cols+1):
                                        tempList.append(World.allCards[ct])
                                        if j % World.cols == 0:
                                                random.shuffle(tempList)
                                                World.cards.append(tempList)
                                        ct += 1                  
                        
        """
         create and add the cards to the screen
         in the correct format
        """
        def createBoard(self):
                x = 65
                y = 40
                card = None

                self.fillCardArray()
                
                if World.level == 1:
                        for i in range(World.totalCards):
                                if World.cards[i] == 1:
                                        card = Card(world = self, x = x+i*95, y = 45,whichImage = 1)
                                elif World.cards[i] == 2:
                                        card = Card(world = self, x = x+i*95, y = 45, whichImage = 2)
                                elif World.cards[i] == 3:
                                        card = Card(world = self, x = x+i*95, y = 45, whichImage = 3)
                                games.screen.add(card)
                else:
                        for i in range(World.rows):
                                for j in range(World.cols):
                                        if World.cards[i][j] == 1:
                                                card = Card(world = self, x=x+j*95,y=y+i*95)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 2:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=2)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 3:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=3)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 4:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=4)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 5:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=5)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 6:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=6)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 7:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=7)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 8:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=8)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 9:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=9)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 10:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=10)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 11:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=11)
                                                games.screen.add(card)
                                        elif World.cards[i][j] == 12:
                                                card = Card(world = self, x=x+j*95,y=y+i*95,whichImage=12)
                                                games.screen.add(card)

class TkPygame:
        
    def __init__(self):

        self.tk_root = tk.Tk()
        self.tk_root.geometry("300x300")
        self.tk_root.title("Memory Game")
        self.tk_root["background"] = "blue"

        self.make_tk_widgets()

        self.tk_root.mainloop()

    def make_tk_widgets(self):
        self.welcome_text = tk.Label(self.tk_root,text="Welcome to the Memory Game!")
        self.welcome_text.pack()

        self.directions = tk.Button(self.tk_root, text="Directions",command=self.toggle_directions)
        self.directions.pack()
        
        self.btn = tk.Button(self.tk_root, text='Start', command=self.toggle_to_game)
        self.btn.pack()

    def toggle_to_game(self):
        self.tk_root.withdraw()
        self.main()

    def toggle_directions(self):
        self.welcome_text.forget()
        self.btn.forget()
        self.directions.forget()

        self.directions1 = tk.Label(self.tk_root, text="Directions:")
        self.directions1.pack()

        self.directions2 = tk.Label(self.tk_root, text="The goal of the game is to\n match the two cards together.\nIf the two cards don't match, they\nwill flip back over.")
        self.directions2.pack()

        self.back = tk.Button(self.tk_root,text="Back",command=self.back_from_directions)
        self.back.pack()

    def back_from_directions(self):
        self.directions1.forget()
        self.directions2.forget()
        self.back.forget()

        self.welcome_text.pack()
        self.directions.pack()
        self.btn.pack()

    def main(self):
        background_image = games.load_image("images/test.jpg", transparent = False)
        
        games.screen.background = background_image
        games.mouse.is_visible = True
        
        world = World()
        world.createBoard()
        
        smallCursor = SmallSprite()
        games.screen.add(smallCursor)
        
        games.screen.mainloop()

TkPygame()

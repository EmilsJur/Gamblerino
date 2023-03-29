from pygame import mixer
import random
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# casino menu
#
#
#
"""root=Tk()
canvas = Canvas(root, width=300, height=160)
image=ImageTk.PhotoImage("c:\\ST01\\users$\\12dejursevics\\Documents\\Gamblerino-main\\Projekts\\backpic.jpg")
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
"""

class GameMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="black") # parent Frame with a black background
        self.master = master # master widget (root window)
        self.pack(fill="both", expand=True) # frame to fill the parent widget
        self.create_widgets() #  function to create the widgets


    def create_widgets(self):
        title_label = tk.Label(self, text="Welcome to the Casino!", font=("Roman", 36), fg="red", bg="black")
        title_label.pack(pady=30)

        blackjack_button = tk.Button(self, text="Blackjack", command=self.play_blackjack, font=("Helvetica", 24), bg="green", fg="black")
        blackjack_button.pack(pady=10)

        slot_button = tk.Button(self, text="Slot Machine", command=self.play_slot, font=("Helvetica", 24), bg="green", fg="black")
        slot_button.pack(pady=10)

        coinflip_button = tk.Button(self, text="Coin Flip", command=self.play_coinflip, font=("Helvetica", 24), bg="green", fg="black")
        coinflip_button.pack(pady=10)

        quit_button = tk.Button(self, text="Quit", command=self.do_quit, font=("Helvetica",20), bg = "red", fg = "black")
        quit_button.pack(pady=10)

        creator_name = tk.Label(self, text="Made By  [Emils] [Davids]", font=("Helvetica",14), fg="red", bg="black")
        creator_name.pack(side='bottom', ipady=25)

    def play_blackjack(self):
        print("Playing Blackjack...")

    def play_slot(self):
        print("Playing Slot Machine...")

    def play_coinflip(self):
        print("Playing Coin Flip...")

    def do_quit(self):
        quit()



# menu dziesma

#mixer.init()
#mixer.music.load("background.mp3")
#mixer.music.play(loops=-1)

"""
import pygame

pygame.init()

file_path = "path/to/your/audio/file.mp3"

pygame.mixer.music.load(file_path)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()
"""

# blackjack
"""
#krasas
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#pygame starts
pygame.init()

# gartums platums ekranam
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Blackjack")

# blackjack
deck = []
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0
game_over = False

# izveido kartis
for suit in suits:
    for rank in ranks:
        deck.append((suit, rank))

# shuffle
random.shuffle(deck)

# sakuma kartis
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# fonts
font = pygame.font.SysFont('Arial', 25, True, False)

# teksta funkcijas
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# funckijas kartu izskatam
def draw_card(card, x, y):
    suit = card[0]
    rank = card[1]
    card_image = pygame.image.load(f"cards/{rank}_{suit}.png")
    screen.blit(card_image, (x, y))

# speles skaitisanas funckijas
def calculate_score(hand):
    score = 0
    num_aces = 0
    for card in hand:
        rank = card[1]
        if rank == "Ace":
            num_aces += 1
            score += 11
        elif rank in ["Jack", "Queen", "King"]:
            score += 10
        else:
            score += int(rank)
    while num_aces > 0 and score > 21:
        score -= 10
        num_aces -= 1
    return score

# speles beigas
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # karti speletajam
                if not game_over:
                    player_hand.append(deck.pop())
                    player_score = calculate_score(player_hand)
                    if player_score > 21:
                        draw_text("Bust!", font, RED, 400, 300)
                        game_over = True
                else:
                    # jauna spele
                    deck = []
                    player_hand = []
                    dealer_hand = []
                    player_score = 0
                    dealer_score = 0
                    game_over = False
                    for suit in suits:
                        for rank in ranks:
                            deck.append((suit, rank))
                    random.shuffle(deck)
                    player_hand.append(deck.pop())
                    dealer_hand.append(deck.pop())
                    player_hand.append(deck.pop())
                    dealer_hand.append(deck.pop())

    # notira ekranu
    screen.fill(WHITE)
 
"""

root = tk.Tk() # root window
root.geometry("600x600") # dimensions of the root window
root.configure(bg="black") # background color of the root window
game_menu = GameMenu(master=root) # instance of the GameMenu class
root.mainloop() # main event loop to display the GUI and handle events

#
#
#
#

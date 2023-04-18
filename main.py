import tkinter as tk
import pygame.mixer
import random
import pygame

# menu dziesma
pygame.mixer.init()
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(loops=-1)

class GameMenu(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Welcome to the Casino!", font=("Roman", 36), fg="red", bg="black").pack(pady=30)

        tk.Button(self, text="Blackjack", command=self.play_blackjack, font=("Helvetica", 24), bg="green", fg="black").pack(pady=10)
        tk.Button(self, text="Slot Machine", command=self.play_slot, font=("Helvetica", 24), bg="green", fg="black").pack(pady=10)
        tk.Button(self, text="Coin Flip", command=self.play_coinflip, font=("Helvetica", 24), bg="green", fg="black").pack(pady=10)
        tk.Button(self, text="Quit", command=self.master.quit, font=("Helvetica", 20), bg="red", fg="black").pack(pady=10)

        tk.Label(self, text="Made By  [Emils] [Davids]", font=("Helvetica", 14), fg="red", bg="black").pack(pady=60, side='right', ipadx=40)

    def play_blackjack(self):
        print("Playing Blackjack...")

    def play_slot(self):
        print("Playing Slot Machine...")

    def play_coinflip(self):
        self.setup_coinflip_game()

    def setup_coinflip_game(self):

        pygame.init()
        pygame.font.init()

        # dimensijas
        window_width = 640
        window_height = 480

        black = (0, 0, 0)
        white = (255, 255, 255)


        window = pygame.display.set_mode((window_width, window_height))

        # tituls
        pygame.display.set_caption("Coin Flip Game")

        font = pygame.font.SysFont(None, 48)
  
        balance = 100

        bet_amount = 10

        heads_image = pygame.image.load("heads.png")
        tails_image = pygame.image.load("tails.png")

        # loop
        running = True
        result = 0
        while running:
            # Check for events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                # check click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # check flip coin
                    if 200 <= mouse_x <= 440 and 300 <= mouse_y <= 340:
                        balance -= bet_amount
                        result = random.randint(0, 1)

                    if result == 0:
                        coin_image = heads_image
                        result_text = "Heads"
                    else:
                        coin_image = tails_image
                        result_text = "Tails"

                    window.blit(coin_image, (260, 100))


                    result_surface = font.render(result_text, True, white)
                    result_rect = result_surface.get_rect(center=(window_width // 2, 220))
                    window.blit(result_surface, result_rect)

                    if result == 0:
                        balance += bet_amount * 2
                    # display all
                    balance_text = f"Balance: ${balance}"
                    balance_surface = font.render(balance_text, True, white)
                    balance_rect = balance_surface.get_rect(center=(window_width // 2, 400))
                    window.blit(balance_surface, balance_rect)

        # flip coin
        flip_coin_text = "Flip Coin"
        flip_coin_surface = font.render(flip_coin_text, True, white)
        flip_coin_rect = flip_coin_surface.get_rect(center=(window_width // 2, 320))
        pygame.draw.rect(window, black, pygame.Rect(200, 300, 240, 40))
        window.blit(flip_coin_surface, flip_coin_rect)

        # update
        pygame.display.flip()

    # Quit
    pygame.quit()

if __name__ == '__main__':
    root = tk.Tk()
    game_menu = GameMenu(master=root)
    game_menu.pack()
    root.mainloop()

# menu dziesma
pygame.mixer.init()
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(loops=-1)



if __name__ == '__main__':
    root = tk.Tk()
    game_menu = GameMenu(master=root)
    game_menu.pack()
    root.mainloop()



"""
def do_quit(self):
    self.master.destroy()
"""

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

"""
root = tk.Tk()  # root window
root.geometry("600x600")  # dimensions of the root window
root.configure(bg="black")  # background color of the root window
game_menu = GameMenu(master=root)  # instance of the GameMenu class
root.mainloop()  # main event loop to display the GUI and handle events
"""


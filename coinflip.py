import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window dimensions
window_width = 640
window_height = 480

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create the window
window = pygame.display.set_mode((window_width, window_height))

# Set the window title
pygame.display.set_caption("Coin Flip Game")

# Set the font
font = pygame.font.SysFont(None, 48)

# Set the initial balance
balance = 100

# Set the bet amount
bet_amount = 10

# Load the images
heads_image = pygame.image.load("heads.png")
tails_image = pygame.image.load("tails.png")

# Set the game loop
running = True

while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the user clicked on the "Flip Coin" button
            if 200 <= mouse_x <= 440 and 300 <= mouse_y <= 340:
                # Subtract the bet amount from the balance
                balance -= bet_amount

                # Randomly generate the result of the coin flip
                result = random.choice(["heads", "tails"])

                # Check if the user won
                if result == "heads":
                    balance += bet_amount * 2
                    result_text = "You won!"
                else:
                    result_text = "You lost."

    # Fill the window with white color
    window.fill(white)
# Draw the "Flip Coin" button
    pygame.draw.rect(window, black, (200, 300, 240, 40))
    flip_coin_text = font.render("Flip Coin", True, white)
    window.blit(flip_coin_text, (240, 305))

    # Draw the balance
    balance_text = font.render("Balance: $" + str(balance), True, black)
    window.blit(balance_text, (10, 10))

    # Draw the result of the coin flip
    if result == "heads":
        window.blit(heads_image, (window_width // 2 - 50, window_height // 2 - 50))
    elif result == "tails":
        window.blit(tails_image, (window_width // 2 - 50, window_height // 2 - 50))

    # Draw the result text
    result_text = font.render(result_text, True, black)
    window.blit(result_text, (window_width // 2 - 75, window_height // 2 + 50))

    # Update the window
    pygame.display.update()

# Quit Pygame
pygame.quit()
import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Game settings
width = 600
height = 400
block_width = 100
block_height = 20
block_speed = 5

# Create the display
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Stacking Game')

# Clock
clock = pygame.time.Clock()

def draw_block(x, y):
    pygame.draw.rect(display, green, [x, y, block_width, block_height])

def gameLoop():
    game_over = False
    block_x = (width - block_width) / 2
    block_y = height - block_height
    falling = True
    stacked_blocks = []  # List to hold stacked blocks
    score = 0
    score_display = pygame.font.SysFont(None, 35)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Stack block on spacebar press
                    if stacked_blocks and abs(block_x - stacked_blocks[-1][0]) > 10:  # Check alignment
                        game_over = True  # End game if not aligned
                    else:
                        stacked_blocks.append((block_x, block_y))
                        block_y = height - block_height  # Reset block position
                        block_x = random.randint(0, width - block_width)  # New block position
                        score += 1
                if event.key == pygame.K_LEFT:  # Move block left
                    block_x -= 10
                if event.key == pygame.K_RIGHT:  # Move block right
                    block_x += 10
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Stack block on left mouse click
                    if stacked_blocks and abs(block_x - stacked_blocks[-1][0]) > 10:  # Check alignment
                        game_over = True  # End game if not aligned
                    else:
                        stacked_blocks.append((block_x, block_y))
                        block_y = height - block_height  # Reset block position
                        block_x = random.randint(0, width - block_width)  # New block position
                        score += 1

        if falling:
            block_y -= block_speed
            if block_y <= 0:
                block_y = height - block_height
                block_x = random.randint(0, width - block_width)
                score += 1
            if block_y >= height - block_height:
                falling = False

        display.fill(white)
        score_text = score_display.render(f'Score: {score}', True, black)
        display.blit(score_text, (10, 10))  # Display the score

        # Draw stacked blocks
        for bx, by in stacked_blocks:
            draw_block(bx, by)

        draw_block(block_x, block_y)
        pygame.display.update()

        clock.tick(30)

    pygame.quit()
    print(f'Game Over! Your final score is: {score}')  # Print final score

gameLoop()

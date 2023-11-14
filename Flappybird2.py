import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Load images
bg_image = pygame.image.load("/Users/ryanlim/Desktop/CS101 COMP SCI/Unit 2/Flappy+Bird+Notes/Flappy Bird Basics/bg.png")
bird_image = pygame.image.load("/Users/ryanlim/Desktop/CS101 COMP SCI/Unit 2/Flappy+Bird+Notes/Flappy Bird Basics/bird1.png")

# Game variables
bird_rect = bird_image.get_rect()
bird_rect.center = (100, HEIGHT // 2)
bird_speed = 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the bird
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird_rect.y -= bird_speed * 2
    else:
        bird_rect.y += bird_speed

    # Draw background and bird
    screen.blit(bg_image, (0, 0))
    screen.blit(bird_image, bird_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

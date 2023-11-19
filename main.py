import pygame
import sys
import random

pygame.init()

# Set up display
width, height = 1720, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("diz")
icon = pygame.image.load("static.png")
pygame.display.set_icon(icon)

# Colors
background_color = (44, 44, 44)
target_color = (0, 207, 255)
text_color = (0, 0, 0)

# Game variables
target_radius = 50
score = 0
missed = 0
font = pygame.font.Font("freesansbold.ttf", 20)  

def draw_target(surface, x, y, alpha):
    pygame.draw.circle(surface, target_color + (alpha,), (x, y), target_radius)

def main():
    global score, missed

    clock = pygame.time.Clock()
    target_x, target_y = random.randint(target_radius, width - target_radius), random.randint(target_radius, height - target_radius)
    alpha = 255  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                distance = (target_x - mouse_x)**2 + (target_y - mouse_y)**2
                if distance < target_radius**2:
                    score += 1
                    target_x, target_y = random.randint(target_radius, width - target_radius), random.randint(target_radius, height - target_radius)
                    alpha = 255  
                else:
                    missed += 1

        screen.fill(background_color)

        draw_target(screen, target_x, target_y, alpha)
        alpha = max(0, alpha - 10) 

        # Display score and missed count
        score_text = font.render(f"Score: {score} | Missed: {missed}", True, text_color)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)  # Adjust the frame rate as needed

if __name__ == "__main__":
    main()

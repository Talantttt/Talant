import pygame
import sys
import math
from datetime import datetime

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")

# Load Mickey Mouse image
mickey_image = pygame.image.load(r"C:\Users\user\Desktop\Pygame\TSIS6\mickeyclock.jpeg")
mickey_rect = mickey_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Clock hands lengths
minutes_hand_length = 100
seconds_hand_length = 150

def draw_clock_hands():
    current_time = datetime.now().time()
    minutes_angle = math.radians((current_time.minute / 60) * 360 - 90)
    seconds_angle = math.radians((current_time.second / 60) * 360 - 90)

    minutes_x = mickey_rect.centerx + minutes_hand_length * math.cos(minutes_angle)
    minutes_y = mickey_rect.centery + minutes_hand_length * math.sin(minutes_angle)
    seconds_x = mickey_rect.centerx + seconds_hand_length * math.cos(seconds_angle)
    seconds_y = mickey_rect.centery + seconds_hand_length * math.sin(seconds_angle)

    pygame.draw.line(screen, (255, 0, 0), mickey_rect.center, (minutes_x, minutes_y), 5)  # Minutes hand
    pygame.draw.line(screen, (0, 0, 255), mickey_rect.center, (seconds_x, seconds_y), 2)  # Seconds hand

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        screen.blit(mickey_image, mickey_rect)
        draw_clock_hands()

        pygame.display.flip()
        
if __name__ == "__main__":
    main()
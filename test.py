import pygame
import ctypes
import os

# Initialize Pygame
pygame.init()

# Get screen information
def get_screen_info():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    screens = [(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))]
    return screens

# Get info for all monitors
screens = get_screen_info()

# Display screen info
print("Available screens:")
for i, screen in enumerate(screens):
    print(f"Screen {i + 1}: {screen[0]}x{screen[1]}")

# Choose the second monitor if available
if len(screens) > 1:
    screen_width, screen_height = screens[1]
else:
    screen_width, screen_height = screens[0]

# Set the position to the top-left corner of the secondary display
primary_display_width = screens[0][0]
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{primary_display_width},0'

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Center Circle Test')

# Define the circle properties
circle_color = (0, 255, 0)  # Green color
circle_radius = 50  # Radius of the circle
circle_center = (screen_width // 2, screen_height // 2)  # Center of the screen

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Draw the circle in the center
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

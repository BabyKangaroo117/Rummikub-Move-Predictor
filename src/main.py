# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

# Set the name of the window
pygame.display.set_caption("Rummikub Move Predictor")

# Start the window at the display's current maximum size and make it resizable
display_info = pygame.display.Info()
screen_width, screen_height = display_info.current_w, display_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
clock = pygame.time.Clock()

test_surface = pygame.Surface((200, 200))

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            # Recreate the display surface at the new size while keeping it resizable
            new_w, new_h = event.w, event.h
            screen = pygame.display.set_mode((new_w, new_h), pygame.RESIZABLE)

        # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    test_surface.fill("blue")
    screen.blit(test_surface, (0, 0))

    # flip() the display to put your work on screen
    pygame.display.update()

    # limits FPS to 60
    clock.tick(60) 

pygame.quit()
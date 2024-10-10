import pygame  # Import the Pygame library
import sys     # Import the sys library for system-specific parameters and functions

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600  # Define the dimensions of the window
screen = pygame.display.set_mode((width, height))  # Create the window with specified dimensions
pygame.display.set_caption('Button Example')  # Set the title of the window

# Define colors (RGB format)
WHITE = (255, 255, 255)       # Color for the background
BLUE = (0, 0, 255)            # Color for the button
LIGHT_BLUE = (173, 216, 230)  # A lighter blue color

# Button properties
button_rect = pygame.Rect(350, 250, 100, 50)  # Create a rectangle for the button
button_text = 'Click Me'  # Text to display on the button
font = pygame.font.Font(None, 36)  # Create a font object
corner_radius = 20  # Radius for rounded corners


# Initialize the clock for frame rate control
clock = pygame.time.Clock()

# Timer variables
button_clicked_time = 0  # Time when the button was clicked
color_change_duration = 10000  # Duration in milliseconds (2 seconds)
button_clicked = False  # Flag to track if the button was clicked

def draw_button():
    """Draws the button and its text on the screen."""
    pygame.draw.rect(screen, BLUE, button_rect)  # Draw button rectangle
    text_surface = font.render(button_text, True, WHITE)  # Render button text
    text_rect = text_surface.get_rect(center=button_rect.center)  # Center the text within the button
    screen.blit(text_surface, text_rect)  # Draw the text on the screen

# Game loop
running = True
while running:
    for event in pygame.event.get():  # Get all events from the event queue
        if event.type == pygame.QUIT:  # Check if the quit event has occurred
            running = False  # Exit the game loop

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse button clicks
            if button_rect.collidepoint(event.pos):  # Check if the mouse clicked within the button's rectangle
                print("Button clicked!")  # Print a message when the button is clicked
                screen.fill(LIGHT_BLUE)  # Change screen color on button click
                button_clicked = True  # Set the flag to True
                button_clicked_time = pygame.time.get_ticks()  # Record the time of the click

    # Check if the button was clicked and the duration has passed
    if button_clicked:
        current_time = pygame.time.get_ticks()  # Get the current time
        if current_time - button_clicked_time > color_change_duration:  # Check if the duration has passed
            screen.fill(WHITE)  # Reset the screen color to white
            button_clicked = False  # Reset the flag

    # Draw the button
    draw_button()

    # Update the display
    pygame.display.flip()  # Refresh the screen to show the new frame

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()  # Uninitialize all Pygame modules
sys.exit()     # Exit the program

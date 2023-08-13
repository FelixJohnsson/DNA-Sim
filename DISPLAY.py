import pygame
import sys
from GENERATE_DNA import generate_chromosome
from ALL_LOCUS_DATA import *
from ALLENES import get_all_attributes


# Define the color mapping
COLOR_MAPPING = {
    'A': (255, 0, 0),   # Red
    'T': (0, 255, 0),   # Green
    'G': (0, 0, 255),   # Blue
    'C': (255, 255, 0)  # Yellow
}

# The DNA sequence
DNA_SEQUENCE = generate_chromosome()
ATTRIBUTES = get_all_attributes(DNA_SEQUENCE)

LOCUS = [globals()[f'LOCI_{i}'] for i in range(1, 401)]

# Window dimensions
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1000

# Gene dimensions
GENE_WIDTH = 15  # 1 pixel wide
GENE_HEIGHT = 25  # Some arbitrary height

# Game world dimensions
WORLD_WIDTH = GENE_WIDTH * len(DNA_SEQUENCE)
WORLD_HEIGHT = WINDOW_HEIGHT

BORDER_SIZE = 1  # Define the border size
BORDER_COLOR = (255, 255, 255)  # Define the border color

# Font settings
FONT_SIZE = 14
FONT_COLOR = (255, 255, 255)  # White

def calculate_gene_color(gene):
    color = (0, 0, 0)
    for nucleotide in gene:
        color = tuple(map(sum, zip(color, COLOR_MAPPING[nucleotide])))
    return tuple(map(lambda x: x // len(gene), color))

class GeneInfoUI:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.gene_info = None

    def update(self, gene_info):
        self.gene_info = gene_info

    def draw(self, screen, font):
        # Draw background rectangle
        pygame.draw.rect(screen, (50, 50, 50), self.rect)

        if self.gene_info:
            # Display gene information
            gene_text = font.render(self.gene_info, True, FONT_COLOR)
            screen.blit(gene_text, (self.rect.x + 10, self.rect.y + 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    font = pygame.font.SysFont('arial', FONT_SIZE)

    camera_offset = [0, 0]
    dragging = False
    old_pos = None

    # Initialize GeneInfoUI at the top center of the screen
    gene_info_ui = GeneInfoUI(WINDOW_WIDTH // 2 - 100, 10, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle mouse button down event
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    old_pos = event.pos
                    dragging = True

            # Handle mouse button up event
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    dragging = False

            # Handle mouse motion event
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    # Calculate the drag distance
                    dx = old_pos[0] - event.pos[0]
                    old_pos = event.pos

                    # Update the camera offset
                    camera_offset[0] += dx
                    camera_offset[0] = max(min(camera_offset[0], WORLD_WIDTH - WINDOW_WIDTH), 0)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the DNA sequence
        for i, gene in enumerate(DNA_SEQUENCE):
            color = calculate_gene_color(gene)
            x = (i * (GENE_WIDTH + 1)) - camera_offset[0]  # Add the 1 pixel separation
            y = WINDOW_HEIGHT // 2  # Middle of the screen

            if 0 <= x < WINDOW_WIDTH:  # Only draw the gene if it's within the window
                # Draw the border (a larger, white rectangle)
                pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(x - BORDER_SIZE, y - BORDER_SIZE, (GENE_WIDTH * 0.75) + (BORDER_SIZE * 2), (GENE_HEIGHT * 0.75) + (BORDER_SIZE * 2)))

                # Draw the colored rectangle on top of the border
                pygame.draw.rect(screen, color, pygame.Rect(x, y, GENE_WIDTH * 0.75, GENE_HEIGHT * 0.75))

                # Draw the gene index above the gene
                #text = font.render(f"Loci {i+1}", True, FONT_COLOR)
                #screen.blit(text, (x, y - GENE_HEIGHT - text.get_height()))

                # Draw the possible alleles above and below the current gene
                for j, allele in enumerate(LOCUS[i % len(LOCUS)]):
                    color = calculate_gene_color(allele)
                    if gene in LOCUS[i % len(LOCUS)]:
                        offset = (GENE_HEIGHT + 1) * (j - LOCUS[i % len(LOCUS)].index(gene))  # Position above or below the current gene with 1 pixel separation
                    else:
                        offset = 0  # If the gene doesn't exist in the list, there's no offset.
                    pygame.draw.rect(screen, color, pygame.Rect(x, y + offset, GENE_WIDTH * 0.75, GENE_HEIGHT * 0.75))

                    # Check if the mouse position is within the gene rect
                mouse_pos = pygame.mouse.get_pos()
                gene_rect = pygame.Rect(x, y, GENE_WIDTH * 0.75, GENE_HEIGHT * 0.75)

                if gene_rect.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                        gene_info = f"Loci {i+1}: {gene}"  # gene information to display
                        gene_info_ui.update(gene_info)

        gene_info_ui.draw(screen, font)
        
        ATTRIBUTE_START_X = 10
        ATTRIBUTE_START_Y = 10
        LINE_SPACING = 15

        y = ATTRIBUTE_START_Y
        for attribute, value in ATTRIBUTES.items():
            text = font.render(f"{attribute}: {value}", True, FONT_COLOR)
            screen.blit(text, (ATTRIBUTE_START_X, y))
            y += LINE_SPACING

        pygame.display.flip()

if __name__ == "__main__":
    main()
import pygame
import random
import time
from GENERATE_DNA import generate_chromosome

PLANT_LOCI_1 = ('AAGCCTGGG', 'AAGGGGCCT', 'CCTAAGGGG', 'CCTGGGAAG', 'GGGAAGCCT', 'GGGCCTAAG')
PLANT_LOCI_2 = ['AAGGCCGCG', 'AAGGCGGCC', 'CCCGCCGGG', 'CCCGGGGCC', 'GCCAAGGCG', 'GCCCCCGGG', 'GCCGCGAAG', 'GCCGGGCCC', 'GCGAAGGCC', 'GCGGCCAAG', 'GGGCCCGCC', 'GGGGCCCCC']
PLANT_LOCI_3 = ['AAAGCCGCG', 'AAAGCGGCC', 'GCCAAAGCG', 'GCCGCGAAA', 'GCGAAAGCC', 'GCGGCCAAA']
PLANT_LOCI_4 = ['AAACCTGCG', 'AAAGCGCCT', 'CCTAAAGCG', 'CCTGCGAAA', 'GCGAAACCT', 'GCGCCTAAA']
PLANT_LOCI_5 = ['ATTCCTGCC', 'ATTGCCCCT', 'CCTATTGCC', 'CCTGCCATT', 'GCCATTCCT', 'GCCCCTATT']
PLANT_LOCI_6 = ['AAGAATGCC', 'AAGGCCAAT', 'AATAAGGCC', 'AATGCCAAG', 'CCCCCTGCG', 'CCCGCGCCT', 'CCTCCCGCG', 'CCTGCGCCC', 'GCCAAGAAT', 'GCCAATAAG', 'GCGCCCCCT', 'GCGCCTCCC']
PLANT_LOCI_7 = ['AAGAATCCT', 'AAGCCTAAT', 'AATAAGCCT', 'AATCCTAAG', 'CCTAAGAAT', 'CCTAATAAG']
PLANT_LOCI_8 = ['AAGCAGGAC', 'AAGGACCAG', 'CAGAAGGAC', 'CAGGACAAG', 'GACAAGCAG', 'GACCAGAAG']
PLANT_LOCI_9 = ['CAACCCCCT', 'CAACCTCCC', 'CCCCAACCT', 'CCCCCTCAA', 'CCTCAACCC', 'CCTCCCCAA']
PLANT_LOCI_10 = ['GACGGGTGA', 'GACTGAGGG', 'GGGGACTGA', 'GGGTGAGAC', 'TGAGACGGG', 'TGAGGGGAC']

HEIGHT_LOCUS = 1, 5, 7
WIDTH_LOCUS = 1, 4, 5
COLOR_LOCUS = 3, 6, 8
LEAF_LOCUS = 5, 6, 9

# Define constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()

# Set up some basic parameters for the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def calculate_attribute(genes, loci):
    ATTRIBUTE = 0
    MAX_ATTRIBUTE = sum(len(l) for l in loci)

    for i in range(len(genes)):
        gene = genes[i]
        for locus in loci:
            if gene in locus:
                ATTRIBUTE += locus.index(gene)

    return ATTRIBUTE / MAX_ATTRIBUTE # A value between 0 and 1, where 0 is the shortest and 1 is the tallest, and 0.5 is average

def get_gene_value(chromosome, locus_indices, base, gene_range):
    genes = [chromosome[i-1] for i in gene_range]
    
    loci = [globals()[f'PLANT_LOCI_{i}'] for i in locus_indices]

    initial_value = calculate_attribute(genes, loci)

    return base + initial_value
    

# New function to interpret PLANT DNA, not CHARACTER DNA
def interpret_plant_dna(CHROMOSOME):
    plant_height_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': HEIGHT_LOCUS,
        'base': 1,
        'gene_range': [HEIGHT_LOCUS[0], HEIGHT_LOCUS[1], HEIGHT_LOCUS[2]],
    }
    plant_width_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': WIDTH_LOCUS,
        'base': 0.5,
        'gene_range': [WIDTH_LOCUS[0], WIDTH_LOCUS[1], WIDTH_LOCUS[2]],
    }
    plant_leaf_params = {
        'chromosome': CHROMOSOME,
        'locus_indices': LEAF_LOCUS,
        'base': 10,
        'gene_range': [LEAF_LOCUS[0], LEAF_LOCUS[1], LEAF_LOCUS[2]],
    }

    plant_height_value = get_gene_value(**plant_height_params) * 100
    plant_width_value = get_gene_value(**plant_width_params) * 10
    leaf_value = get_gene_value(**plant_leaf_params)


    attributes = {
        'height': round(int(plant_height_value), 2),
        'width': round(int(plant_width_value), 2),
        'color': (0, 255, 0),
        'leaf': leaf_value
    }

    return attributes

def draw_branch(x_position, y_position, attributes, color, length):
    # Is it growing on the left or right side of the stem?
    growing_direction = random.random() < 0.5

    # Branch thickness is proportional to length
    branch_thickness = max(1, int(attributes['width'] * length * 0.005))

    # Adjust the color of the branch
    branch_color = (max(0, color[0] - random.randint(0, 50)),
                    max(0, color[1] - random.randint(0, 50)),
                    max(0, color[2] - random.randint(0, 50)))

    leaf_color = (34, 139, 34) # green color

    for i in range(length):
        if growing_direction:
            if i % 2 == 0:
                x_position -= random.randint(1, 3)
        else:
            if i % 2 == 0:
                x_position += random.randint(1, 3)

        pygame.draw.rect(screen, branch_color, (x_position, y_position - i, branch_thickness, 1))

        # Draw a leaf every 10 pixels along the branch
        if i % 5 == 0:
            pygame.draw.circle(screen, leaf_color, (x_position, y_position - i), branch_thickness * 2)

# Function to draw plant based on DNA
def draw_plant(dna, x_position):
    attributes = interpret_plant_dna(dna)
    # Brown stem color
    plant_stem_color = (139, 69, 19)

    # Draw the stem
    for i in range(attributes['height']):
        branch_chance = 0.1

        # x_position += 1 is a diagonal line to the right
        # Randomize the x_position every tenth time to make the stem look more natural
        if i % 10 == 0:
            x_position += random.randint(-1, 1)
        pygame.draw.rect(screen, plant_stem_color, (x_position, SCREEN_HEIGHT - i, attributes['width'], 1))
        
        # Draw branches
        if random.random() < branch_chance:
            length = random.randint(10, 50)
            draw_branch(x_position, SCREEN_HEIGHT - i, attributes, plant_stem_color, length)



# Clear the screen
screen.fill((240, 240, 240))

# Generate a DNA and draw a plant based on it
DNA = generate_chromosome()
draw_plant(DNA[0 : 10], SCREEN_WIDTH / 2)

# Flip the display
pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
import pygame
import random
from GENERATE_DNA import generate_chromosome
from ALLENES import get_all_attributes
import numpy as np

class Agent:
    def __init__(self, learning_rate=0.01, discount_factor=0.95, exploration_rate=1.0, iterations=10000):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay_rate = exploration_rate / iterations

        # Initialize Q-table with zeros
        self.q_table = np.zeros((WIDTH, HEIGHT, 4))

    def get_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.randint(4)  # Explore: select a random action
        else:
            return np.argmax(self.q_table[state[0], state[1]])  # Exploit: select the action with max value (Q) for current state

    def update_q(self, state, action, reward, new_state):
        self.q_table[state[0], state[1], action] = self.q_table[state[0], state[1], action] * (1 - self.learning_rate) + \
            self.learning_rate * (reward + self.discount_factor * np.max(self.q_table[new_state[0], new_state[1]]))

        if self.exploration_rate > 0:
            self.exploration_rate -= self.exploration_decay_rate

        
# Set the dimensions of the window
WIDTH, HEIGHT = 800, 600

AMOUNT_OF_CREATURES = 5

class Creature:
    def __init__(self, name):
        self.agent = Agent()
        self.DNA = generate_chromosome() # 400 locus DNA sequence (1200 codons)
        print('Generated ' + name + "'s DNA")
        self.name = name
        self.attributes = get_all_attributes(self.DNA)
        self.age = random.randint(18, 50)

        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

    # FROM DNA SEQUENCE
        self.height = self.attributes['height']
        self.torso_length = self.attributes['torso_length']
        self.arm_length = self.attributes['arm_length']
        self.leg_length = self.attributes['leg_length']

        self.musculature_type = self.attributes['musculature_value']
        self.metabolism = self.attributes['metabolism_value']
        self.flexibility = self.attributes['flexibility_value']
        self.pain_tolerance = self.attributes['pain_tolerance_value']
        self.vision = self.attributes['vision_value']
        self.hearing = self.attributes['hearing_value']
        self.regeneration = self.attributes['regeneration_value']
        self.blood_type = self.attributes['blood_type_value']
        self.brain_type = self.attributes['brain_type_value']
        self.lung_capacity = self.attributes['lung_capacity_value']

        self.hair_color = self.attributes['hair_color_value']
        self.hair_type = self.attributes['hair_type_value']
        self.eye_color = self.attributes['eye_color_value']

        self.weight = 0

        self.strength = 0
        self.agility = 0

        self.intelligence = 0
        self.charisma = 0

    # FROM DNA SEQUENCE AND ENVIRONMENT
        self.loyalty = 0
        self.morale = 0
        self.discipline = 0
        self.bravery = 0
        self.aggression = 0

        self.herbivore = 0
        self.carnivore = 0
        self.omnivore = 1

        self.traits = []
        self.skills = []
        self.abilities = []
        
        self.hp = 0 # Should be a calculation all all the attributes and traits
        self.damage = 0 # Should be a calculation all all the attributes and traits
        self.defence = 0 # Should be a calculation all all the attributes and traits
        self.speed = 0 # Should be a calculation all all the attributes and traits

    # FROM THE ENVIRONMENT
        self.equipment = []
        self.inventory = []

        self.battle_experience = 0
        self.battle_kills = 0
        self.battle_wins = 0
        self.battle_wounds = 0

    def move(self):
        # Get current state
        state = (self.x, self.y)

        # Get action from agent
        action = self.agent.get_action(state)

        # Apply action
        if action == 0:   # Move up
            self.y -= 1
        elif action == 1: # Move down
            self.y += 1
        elif action == 2: # Move left
            self.x -= 1
        elif action == 3: # Move right
            self.x += 1

        # Get new state and reward
        new_state = (self.x, self.y)
        reward = self.get_reward()

        # Update Q-values
        self.agent.update_q(state, action, reward, new_state)

        # Keep the creature within the screen boundaries
        self.x = max(0, min(WIDTH, self.x))
        self.y = max(0, min(HEIGHT, self.y))

    def get_reward(self):
        return 1 if self.x == WIDTH - 1 and self.y == HEIGHT - 1 else 0

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 5)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, screen):
        screen.fill((152, 251, 152))

world = World(WIDTH, HEIGHT)
creatures = [Creature(f"Creature {i}") for i in range(AMOUNT_OF_CREATURES)]

def main():
    pygame.init()
    pygame.display.set_caption("Evolution Simulation")
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        world.draw(WINDOW)

        for creature in creatures:
            creature.move()
            creature.draw(WINDOW)
        
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
 
if __name__ == "__main__":
    main()

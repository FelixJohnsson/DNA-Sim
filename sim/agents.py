import random
import pygame
from collections import defaultdict

# Pygame settings
WINDOW_SIZE = [800, 800]
TILE_SIZE = 16

class Tile:
    def __init__(self):
        self.value = 0

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Tile() for _ in range(width)] for _ in range(height)]
        self.agents = []

    def place_food(self, x, y):
        self.grid[y][x].value = 1

    def add_agent(self, agent):
        self.agents.append(agent)

    def update(self):
        # Randomly grow food
        if random.random() < 0.01:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.place_food(x, y)

        # Update agents
        for agent in self.agents:
            agent.update()

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                color = (0, 255, 0) if self.grid[y][x].value == 1 else (255, 255, 255)
                pygame.draw.rect(screen, color, [x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE])

class Agent:
    def __init__(self, x, y, environment):
        self.x = x
        self.y = y
        self.environment = environment
        self.food_collected = 0
        self.q_table = self.initialize_q_table()  # Initialize Q-table instead of policy

    def initialize_q_table(self):
        # Initialize a Q-table that maps each possible state-action pair to a value
        q_table = defaultdict(lambda: 0)  # Default value is 0 for all state-action pairs
        return q_table

    def choose_action(self, observation):
        # Calculate the number of food items in the observation
        num_food = observation.count(1)

        # Choose an action based on the Q-values of the possible actions and the number of food items
        possible_actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q_values = [self.q_table[((self.x, self.y), action)] + num_food for action in possible_actions]
        self.last_action = possible_actions[q_values.index(max(q_values))]  # Store the chosen action
        return self.last_action  # Return the chosen action
    
    def update_q_table(self, reward, action, observation):
        # Convert the observation list to a tuple
        observation = tuple(observation)

        # Update the Q-table based on the received reward and the maximum Q-value of the new state
        old_value = self.q_table[(observation, action)]
        max_new_value = max([self.q_table[(observation, action)] for action in [(0, 1), (0, -1), (1, 0), (-1, 0)]])
        self.q_table[(observation, action)] = old_value + 0.1 * (reward + 0.9 * max_new_value - old_value)
    
    def observe(self):
        # Get the current observation. 5x5 grid centered on the agent
        OBSERVATIONAL_SPACE = 5
        observation = []
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                x = self.x + dx
                y = self.y + dy

                # If the agent is at the edge of the environment, pad with zeros
                if 0 <= x < self.environment.width and 0 <= y < self.environment.height:
                    # If the current position is the agent's position, mark with a 2
                    if (x, y) == (self.x, self.y):
                        observation.append(2)
                    # Otherwise, use the value of the tile
                    else:
                        observation.append(self.environment.grid[y][x].value)
                else:
                    observation.append(0)
        
        return observation

    def update_policy(self, reward):
        # Update the policy based on the received reward
        # This is a very simplified example; in a real RL algorithm, you would also consider the future expected rewards
        if reward > 0:
            # If the reward was positive, increase the probability of the last action
            self.policy[(self.x, self.y)][self.last_action_index] = min(1, self.policy[(self.x, self.y)][self.last_action_index] + 0.1)
        else:
            # If the reward was negative, decrease the probability of the last action
            self.policy[(self.x, self.y)][self.last_action_index] = max(0.01, self.policy[(self.x, self.y)][self.last_action_index] - 0.1)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < self.environment.width and 0 <= new_y < self.environment.height:
            self.last_x = self.x  # Store the current position
            self.last_y = self.y
            self.x = new_x
            self.y = new_y

    def interact(self):
        tile = self.environment.grid[self.y][self.x]
        if tile.value == 1:
            tile.value = 0
            self.food_collected += 1
            print(f"Food collected: {self.food_collected}")
            return 1 - 0.01 * (abs(self.x - self.last_x) + abs(self.y - self.last_y))  # Reward is decreased based on the distance traveled
        else:
            return -0.01 * (abs(self.x - self.last_x) + abs(self.y - self.last_y))  # Penalty for moving without collecting food

    def update(self):
        # Get current observation
        observation = self.observe()

        # Choose an action
        dx, dy = self.choose_action(observation)

        # Perform the action
        self.move(dx, dy)

        # Receive a reward
        reward = self.interact()

        # Update the Q-table
        self.update_q_table(reward, self.last_action, observation)


    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), [self.x*TILE_SIZE + TILE_SIZE//2, self.y*TILE_SIZE + TILE_SIZE//2], TILE_SIZE//2)

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Create environment and place some food
    environment = Environment(WINDOW_SIZE[0]//TILE_SIZE, WINDOW_SIZE[1]//TILE_SIZE)
    environment.place_food(5, 5)

    # Create agents
    for _ in range(5):
        x = random.randint(0, environment.width - 1)
        y = random.randint(0, environment.height - 1)
        agent = Agent(x, y, environment)
        environment.add_agent(agent)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        environment.update()

        screen.fill((0, 0, 0))
        environment.draw(screen)
        for agent in environment.agents:
            agent.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
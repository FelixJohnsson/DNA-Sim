import gym
import numpy as np
from gym import spaces
from stable_baselines3 import PPO

class MultiAgentGridWorldEnvironment(gym.Env):
    def __init__(self, grid_size, num_agents):
        super(MultiAgentGridWorldEnvironment, self).__init__()

        self.grid_size = grid_size
        self.num_agents = num_agents

        self.action_space = spaces.MultiDiscrete([4]*num_agents)  # Up, Down, Left, Right for each agent
        self.observation_space = spaces.Box(low=0, high=1, shape=(self.grid_size, self.grid_size, self.num_agents), dtype=np.int32)

        self.agent_positions = np.zeros((self.num_agents, 2), dtype=np.int32)

    def step(self, actions):
        for i in range(self.num_agents):
            if actions[i] == 0:  # Up
                self.agent_positions[i, 0] = max(self.agent_positions[i, 0] - 1, 0)
            elif actions[i] == 1:  # Down
                self.agent_positions[i, 0] = min(self.agent_positions[i, 0] + 1, self.grid_size - 1)
            elif actions[i] == 2:  # Left
                self.agent_positions[i, 1] = max(self.agent_positions[i, 1] - 1, 0)
            elif actions[i] == 3:  # Right
                self.agent_positions[i, 1] = min(self.agent_positions[i, 1] + 1, self.grid_size - 1)

        rewards = self._calculate_rewards()
        done = self._check_done()
        return self._get_obs(), rewards, done, {}

    def reset(self):
        self.agent_positions = np.random.randint(self.grid_size, size=(self.num_agents, 2))
        return self._get_obs()

    def _get_obs(self):
        obs = np.zeros((self.grid_size, self.grid_size, self.num_agents), dtype=np.int32)
        for i in range(self.num_agents):
            obs[self.agent_positions[i, 0], self.agent_positions[i, 1], i] = 1
        return obs

    def _calculate_rewards(self):
        # Dummy reward function: reward is -1 for all agents
        return -np.ones(self.num_agents, dtype=np.int32)

    def _check_done(self):
        # Dummy termination condition: episode is never done
        return False

def main():
    env = MultiAgentGridWorldEnvironment(grid_size=10, num_agents=5)
    model = PPO("MlpPolicy", env, verbose=1)

    model.learn(total_timesteps=10000)

if __name__ == "__main__":
    main()
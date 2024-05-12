import gymnasium as gym
from stable_baselines3 import PPO
import torch

# Load the saved model
ppo_model = PPO.load("./models/ppo_sb3_model.keras")

# Create the environment
env = gym.make("highway-v0", render_mode="human")
# env = gym.make("highway-fast-v0", render_mode="human")
# env = gym.make("roundabout-v0", render_mode="human")


env.config["duration"] = 360


# Reset the environment
observation, info = env.reset(seed=42)

# Define the loop for interacting with the environment
for _ in range(1000):
    # Use the model to select an action
    action, _ = ppo_model.predict(observation)

    # Step through the environment with the selected action
    observation, reward, terminated, truncated, info = env.step(action)

    # If the episode is terminated or truncated, reset the environment
    if terminated or truncated:
        observation, info = env.reset()

# Close the environment
env.close()

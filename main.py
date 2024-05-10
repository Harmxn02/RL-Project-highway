"""
> if you get this error:

Cannot find implementation or library stub for module named "gymnasium"mypy

> in the bottom bar, change terminal to a Python environment that has Gymnasium pip installed

"""



#### IDEA FOR PRESENTATION
# HAVE THIS RUN IN THE BACKGROUND WHILE YOU INTRODUCE THE PROJECT


import gymnasium as gym
env = gym.make("highway-v0", render_mode="human")
observation, info = env.reset(seed=42)
for _ in range(1000):
   action = env.action_space.sample()  # this is where you would insert your policy
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()

env.close()
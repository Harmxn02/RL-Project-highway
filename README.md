# RL Project: Highway

## Assignment Tasks

1. Work out explanations as to why I chose certain algorithms
2. Compare the algorithms (number of episodes, time to train)
3. Choose the best algorithm
4. Make a presentation to introduce the project
    - Explain environment
    - Chosen algorithmes and why
    - Comparison between algorithms
    - Show the result (random episodes versus the trained result)

## Assignment context

In this project I will train an agent to navigate on a highway, and hopefully avoid crashing. The OpenAI Gymnasium environment is called [HighwayEnv](https://github.com/Farama-Foundation/HighwayEnv) and is made by [Farama-Foundation](https://github.com/Farama-Foundation/).

## Contents of this repository

In this repository you will find all project files for a project I had for the course **Reinforcement Learning**.

## Folder structure

### Files

1. `main.ipynb` contains all the code for the models
2. `main.py` contains the code for presentation's introduction-simulation

### Models

`/models/` contains all the models

1. `~/dqn_sb3_model.keras` contains the DQN model (.keras)
2. `~/ppo_sb3_model.keras` contains the PPO model (.keras)
3. `~/a2c_sb3_model.keras` contains the PPO model (.keras)
4. `~/dqn_sb3_model.zip` contains the DQN model (stable baselines3's default format)
5. `~/ppo_sb3_model.zip` contains the PPO model (stable baselines3's default format)
6. `~/a2c_sb3_model.zip` contains the PPO model (stable baselines3's default format)

### Training Videos

`/videos/` contains all the models (saved as `.mp4`)

1. `~/DQN-stable-baselines3/` contains the training videos for the DQN model
2. `~/PPO-stable-baselines3` contains the training videos for the PPO model
3. `~/A2C-stable-baselines3` contains the training videos for the A2C model

**BONUS**. `~/random` contains the training video where the agent randomly picks actions from the action space. Spoiler, it's terribe :)

### Presentation Files

`/presentation/` contains the notebook used for making plots (used in the presentation)

&nbsp;

> Harman Singh

### Time spent on this project

| Day         | Time spent | Start time | End time |
| ----------- | ---------- | ---------- | -------- |
| Fri, 10 May | 2h11       | 17h09      | 19h20    |
| Sun, 12 May | 2h15       | 15h15      | 17h30    |
| Sun, 12 May | 0h15       | 18h55      | 19h10    |
| Sun, 12 May | 0h35       | 20h55      | 22h00    |

### **TOTAL**: 5h46

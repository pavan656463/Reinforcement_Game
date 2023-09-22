# Reinforcement_Game
Model.py is the runnable file<br/>
Learning.py file is containing the learning model for the given game
# Applied Model free learning i.e, Q-LEARNING model for training

# Guide
There are 2 options provided Human vs Computer and Train<br/>
To exit game please use Esc(button) or Quit <br/>

# Algorithm
Initially we have to import required libraries<br/>
-->**Pygame**:This library includes modules for playing sound, drawing graphics, handling mouse inputs,<br/>
          and creating client-side applications that can be wrapped in standalone executables.<br/>
-->**Random**:This module implements pseudo-random number generators for various distributions.<br/>
Model Training:,<br/>
->So the main aim of this game is to arrange the coins in an order where the 4 coins of same color should<br/>
come together either vertically or horizontally.<br/>
->Initially the computer and the human will be played randomly.<br/>
->Then the actions will be recorded by the model in the Q-Table.<br/> 
->Then the model will play according to the best actions recorded in Q-table.<br/>
->Later the trained model will be deployed.<br/>

# Qtable 
-> Qtable records every actions of previous game<br/>
-> Which helps to make next decision <br/>
-> All records are store **q_table.txt**<br/>

# Train
Mainly training is done in Q learning <br/>
there will be Player 1 and Player 2, both players will Bots(Computer) based on **it will train itself(self-learning)**<br/>
To exit Train please use Esc 


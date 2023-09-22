import random

"""This class that represents a player in the game(Bot Player)"""
class Player():
    def __init__(self, coin_type):
        """
        Initialize a player with their coin type
        """
        self.coin_type = coin_type

    def complete_move(self):
        """
        A method to make a move and update any learning parameters if any
        """
        pass

    def get_coin_type(self):
        """
        Return the coin type of the player
        """
        return self.coin_type

    def set_coin_type(self, coin_type):
        """
        Set the coin type of a player
        """
        self.coin_type = coin_type


import random
import pickle

class QLearningPlayer(Player):
    """A class that represents an AI using Q-learning algorithm"""

    def __init__(self, coin_type, epsilon=0.2, alpha=0.3, gamma=0.9, q_table_file=None):
        """
        Initialize a Q-learner with parameters epsilon, alpha, gamma, and its coin type.
        If q_table_file is provided, it loads the Q-table from the file.
        """
        Player.__init__(self, coin_type)
        self.q = {}
        self.epsilon = epsilon  # e-greedy chance of random exploration
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor for future rewards
        if q_table_file:
            self.load_q_table(q_table_file)  # Load Q-table from file if provided

    def save_q_table(self, filename):
        """
        Save the Q-table to a text file.
        """
        with open(filename, 'w') as file:
            for key, value in self.q.items():
                file.write(f"{key}: {value}\n")

    def load_q_table(self, filename):
        """
        Load the Q-table from a text file.
        """
        self.q = {}
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(": ")
                key = eval(parts[0])  # Convert the key back to a tuple
                value = float(parts[1])
                self.q[key] = value


    def getQ(self, state, action):
        """
        Return a probability for a given state and action where the greater
        the probability the better the move
        """
        # encourage exploration; "optimistic" 1.0 initial values

        if self.q.get((state, action)) is None:
            self.q[(state, action)] = 1.0
        return self.q.get((state, action))

    def choose_action(self, state, actions):
        """
        Return an action based on the best move recommendation by the current
        Q-Table with a epsilon chance of trying out a new move
        """
        current_state = state

        if random.random() < self.epsilon:  # explore!
            chosen_action = random.choice(actions)
            return chosen_action

        qs = [self.getQ(current_state, a) for a in actions]
        maxQ = max(qs)

        if qs.count(maxQ) > 1:
            # more than 1 best option; choose among them randomly
            best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
            i = random.choice(best_options)
        else:
            i = qs.index(maxQ)

        return actions[i]

    def learn(self, board, actions, chosen_action, game_over, game_logic, q_table_file='q_table.txt'):
        """
        To determine the reward based on its current chosen action and update the Q table,
        we calculate the reward received for the action taken.
        This reward is then used to update the Q table by incorporating the maximum future reward that can be obtained based on the resulting state resulting from the chosen action.
        This process helps the agent learn and improve its decision-making over time.
        q_table_file is provided, it loads the Q-table from the file before learning.
        """

        if q_table_file:
            self.load_q_table(q_table_file)  # Load Q-table from file if provided

        reward = 0
        if game_over:
            win_value = game_logic.get_winner()
            if win_value == 0:
                reward = 0.5
            elif win_value == self.coin_type:
                reward = 1
            else:
                reward = -2
        prev_state = board.get_prev_state()
        prev = self.getQ(prev_state, chosen_action)
        result_state = board.get_state()
        maxqnew = max([self.getQ(result_state, a) for a in actions])
        self.q[(prev_state, chosen_action)] = prev + self.alpha * ((reward + self.gamma * maxqnew) - prev)
        if q_table_file:
            self.save_q_table(q_table_file)  # Save Q-table to file after learning

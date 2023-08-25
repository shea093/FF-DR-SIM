# contestant.py

import config
import random

class Contestant:
    # Update when adding new attributes to __init__
    def __init__(self, id, name, stats):
        """
        Initialize a Contestant object with a name and a dictionary of stats.

        :param name: The name of the contestant.
        :param stats: A dictionary containing the contestant's stats.
        """
        self.id = id
        self.name = name
        self.stats = stats  # Exclude 'name' from columns
        test =1
        # self.stats = stats

    def perform_challenge(self, challenge):
        total_bias = sum(challenge.biases.values())
        total_stat = sum(
            (challenge.biases[attr] * self.stats[attr])
            for attr in challenge.biases
        )

        # Calculate the scaled challenge score out of 10
        challenge_score = (total_stat / total_bias) * 10
        challenge_score = self.apply_randomization(challenge_score)

        return challenge_score

    @staticmethod
    def apply_randomization(base_score):
        """
        Apply randomization to a base score based on randomization percentage from config.

        :param base_score: The base score before randomization.
        :return: The score after applying randomization.
        """
        randomization_factor = random.uniform(1 - config.RANDOM_VARIABILITY, 1 + config.RANDOM_VARIABILITY)
        randomized_score = base_score * randomization_factor
        return randomized_score

    def __str__(self):
        avg_stats = sum(self.stats.values()) / len(self.stats)
        return f"{self.name} (Avg Stats: {avg_stats:.2f})"
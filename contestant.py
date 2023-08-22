# contestant.py

import config
import random

class Contestant:
    # Update when adding new attributes to __init__
    def __init__(self, **kwargs):
        """
        Initialize a Contestant object based on the provided keyword arguments.

        :param kwargs: Keyword arguments representing the contestant's attributes.
                       The keys should match the columns defined in DB_COLUMNS.
        """
        for column in config.DB_COLUMNS:
            # Use kwargs.get(column, 0) to retrieve the value for the given column from kwargs.
            # If the column is not present in kwargs, the default value of 0 is used.
            setattr(self, column, kwargs.get(column, 0))

    def perform_challenge(self, challenge):
        """
        Simulate a contestant's performance in a challenge with randomization.

        :param challenge: The Challenge object for the episode.
        :return: A simulated challenge score based on contestant attributes, challenge biases, and randomization.
        """
        # Calculate challenge score based on biases and contestant stats
        base_challenge_score = sum(
            (challenge.biases[attr] * getattr(self, attr))
            for attr in challenge.biases
        )

        # Apply randomization using the apply_randomization method
        challenge_score = self.apply_randomization(base_challenge_score)

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
# contestant.py

import sqlite3
import config
import random

class Contestant:
    # Update when adding new attributes to __init__
    _DB_COLUMNS = ['name', 'charisma', 'creativity', 'runway_presence', 'performance_skills', 'sewing_and_crafting',
                   'comedy', 'drama_and_emotion', 'adaptability', 'teamwork', 'confidence', 'lipsyncing']

    def __init__(self, id, name, charisma, creativity, runway_presence, performance_skills,
                 sewing_and_crafting, comedy, drama_and_emotion, adaptability,
                 teamwork, confidence, lipsyncing):
        self.id = id
        self.name = name
        self.charisma = charisma
        self.creativity = creativity
        self.runway_presence = runway_presence
        self.performance_skills = performance_skills
        self.sewing_and_crafting = sewing_and_crafting
        self.comedy = comedy
        self.drama_and_emotion = drama_and_emotion
        self.adaptability = adaptability
        self.teamwork = teamwork
        self.confidence = confidence
        self.lipsyncing = lipsyncing
        self.score = 0  # Initialize score to 0

    def perform_challenge(self, challenge):
        contestant_score = self.calculate_contestant_score(challenge.attribute_biases)
        randomized_score = self.apply_randomization(contestant_score)

        return randomized_score

    def calculate_contestant_score(self, attribute_biases):
        total_bias = sum(attribute_biases[attr] * getattr(self, attr) for attr in attribute_biases)
        return max(0, min(100, total_bias))

    def apply_randomization(self, score):
        random_factor = random.uniform(1 - config.RANDOM_VARIABILITY, 1 + config.RANDOM_VARIABILITY)
        randomized_score = score * random_factor
        return max(0, min(100, randomized_score))
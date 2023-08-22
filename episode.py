import sqlite3

class Episode:
    def __init__(self, id, episode_number):
        self.id = id
        self.episode_number = episode_number

    def __init__(self, episode_number, contestants, challenge):
        self.episode_number = episode_number
        self.contestants = contestants
        self.challenge = challenge
        self.scores = {}  # Dictionary to store contestant scores

    def run_episode(self):
        for contestant in self.contestants:
            contestant_score = contestant.perform_challenge(self.challenge)
            self.scores[contestant] = contestant_score
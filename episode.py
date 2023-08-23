import random
class Episode:
    def __init__(self, id, contestants, challenge):
        """
        Initialize an Episode object with specified contestants and challenge.

        :param id: The ID of the episode.
        :param contestants: A list of Contestant objects participating in the episode.
        :param challenge: The Challenge object for the episode.
        """
        self.id = id
        self.contestants = contestants
        self.challenge = challenge
        self.scores = {}  # A dictionary to store scores for each contestant
        self.high_group = []
        self.low_group = []
        self.safe_group = []

    def calculate_challenge_scores(self):
        """
        Calculate challenge scores for each contestant in the episode and store them in self.scores.
        """
        for contestant in self.contestants:
            # Call the perform_challenge method of Contestant to get the challenge score
            contestant_score = contestant.perform_challenge(self.challenge)
            self.scores[contestant] = contestant_score


    def calculate_score_percentile(self, num_contestants, percentile):
        """
        Calculate the score value at the given percentile.

        :param num_contestants: The total number of contestants.
        :param percentile: The desired percentile (0.0 to 1.0).
        :return: The score value at the specified percentile.
        """
        sorted_scores = sorted(self.scores.values(), reverse=True)
        index = int(num_contestants * percentile)
        return sorted_scores[index]

    def categorize_contestants(self):
        num_contestants = len(self.contestants)

        if num_contestants <= 6:
            # 70% chance of top 3, else top 2
            if random.random() < 0.7:
                num_top = 3
            else:
                num_top = 2
            num_bottom = 3
        elif 7 <= num_contestants <= 12:
            # 80% chance of top 3, else top 4
            if random.random() < 0.8:
                num_top = 3
            else:
                num_top = 4
            num_bottom = 3
        else:
            num_top = 4
            # 70% chance of bottom 3, else bottom 4
            if random.random() < 0.7:
                num_bottom = 3
            else:
                num_bottom = 4

        sorted_contestants = sorted(self.contestants, key=lambda c: self.scores[c], reverse=True)

        self.high_group = sorted_contestants[:num_top]
        self.low_group = sorted_contestants[-num_bottom:]
        self.safe_group = [c for c in self.contestants if c not in self.high_group and c not in self.low_group]
    def __str__(self):
        """
        Return a string representation of the Episode object.

        :return: A formatted string containing episode details.
        """
        contestant_scores = "\n".join(
            f"{contestant.name}: {self.scores[contestant]:.2f}"
            for contestant in self.contestants
        )
        return f"Episode {self.id} - Challenge: {self.challenge.name}\n{contestant_scores}"
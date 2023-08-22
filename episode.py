

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

    def calculate_challenge_scores(self):
        """
        Calculate challenge scores for each contestant in the episode and store them in self.scores.
        """
        for contestant in self.contestants:
            # Call the perform_challenge method of Contestant to get the challenge score
            contestant_score = contestant.perform_challenge(self.challenge)
            self.scores[contestant] = contestant_score


    def categorize_contestants(self):
        """
        Categorize contestants based on their scores into different groups.
        """
        high_cutoff = self.calculate_score_percentile(0.25)
        low_cutoff = self.calculate_score_percentile(0.75)

        self.high_group = [contestant for contestant, score in self.scores.items() if score >= high_cutoff]
        self.safe_group = [contestant for contestant, score in self.scores.items() if low_cutoff <= score < high_cutoff]
        self.low_group = [contestant for contestant, score in self.scores.items() if score < low_cutoff]

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
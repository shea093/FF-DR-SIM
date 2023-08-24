import random
from contestant import Contestant
import config


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
        self.winners = []
        self.bottom2 = []
        self.eliminated = []

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

        # Clear existing group assignments
        self.high_group = []
        self.low_group = []
        self.safe_group = []

        # Track assigned contestants
        assigned_contestants = []

        # Assign contestants to groups
        for contestant in sorted_contestants:
            if contestant in assigned_contestants:
                continue

            if len(self.high_group) < num_top:
                self.high_group.append(contestant)
                assigned_contestants.append(contestant)
            elif len(self.low_group) < num_bottom:
                self.low_group.append(contestant)
                assigned_contestants.append(contestant)
            else:
                self.safe_group.append(contestant)
                assigned_contestants.append(contestant)

    def determine_winner(self):
        # Sort contestants by scores in descending order
        sorted_contestants = sorted(self.contestants, key=lambda c: self.scores[c], reverse=True)

        # Determine the number of winners (1 or 2)
        num_winners = 1 if random.randint(1,100) > config.DOUBLE_WINNER_CHANCE else 2

        # Assign the highest scoring contestants as winners
        winners = sorted_contestants[:num_winners]

        # Remove winners from the high group
        self.high_group = [c for c in self.high_group if c not in winners]

        # Store winners in the self.winners attribute
        self.winners = winners

        return winners

    def determine_bottom_2(self):
        # Define the modular formula function
        def bottom2_formula(group, num_picks):
            # Implement your modular formula here
            # For now, let's just randomly choose contestants
            return random.sample(group, num_picks)

        # Use the modular formula to determine the bottom 2 from the LOW group
        bottom_2 = bottom2_formula(self.low_group, num_picks=2)

        # Remove winners from the high group
        self.low_group = [c for c in self.low_group if c not in bottom_2]

        # Store winners in the self.winners attribute
        self.bottom2 = bottom_2
        return bottom_2

    def lipsync(self, contestant1: Contestant, contestant2: Contestant  ):
        random_factor1 = random.uniform(config.min_lipsync, config.max_lipsync)
        random_factor2 = random.uniform(config.min_lipsync, config.max_lipsync)

        randomized_num1 = contestant1.stats["lipsyncing"] * random_factor1
        randomized_num2 = contestant2.stats["lipsyncing"] * random_factor2

        if randomized_num1 > randomized_num2:
            return [contestant1,contestant2]
        else:
            return [contestant2, contestant1]

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
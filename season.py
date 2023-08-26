from episode import Episode
from challenge import Challenge
from contestant import Contestant


class Season:
    def __init__(self, id, contestants, challenges, finale_type):
        self.id = id
        self.episodes = []
        self.contestants = contestants  # All contestants that start the season
        self.current_contestants = contestants.copy()  # Contestants currently in the competition
        self.challenges = challenges
        self.finale_type = finale_type  # Top 3 or Top 4

    def add_episode(self, episode):
        """Adds an episode to the season."""
        self.episodes.append(episode)

    def get_eliminated_contestant(self, episode):
        """Returns the eliminated contestant based on episode performance."""
        # Placeholder logic to get the eliminated contestant (e.g., lowest score)
        # This can be expanded based on specific criteria
        return min(episode.scores, key=episode.scores.get)

    def simulate_episode(self, challenge):
        """Simulates an episode, determining winners and eliminated contestants."""
        # Create a new episode
        episode = Episode(len(self.episodes) + 1, self.current_contestants, challenge)

        # Categorize contestants and determine eliminated contestant

        # Ensure scores are set for all contestants
        for contestant in self.current_contestants:
            episode.scores[contestant] = contestant.perform_challenge(challenge)

        if len(episode.contestants) > 4:
            episode.categorize_contestants()
            episode.determine_bottom_2()
            episode.determine_winner()
        else:
            sorted_contestants = sorted(episode.contestants, key=lambda c: episode.scores[c], reverse=True)
            episode.bottom2 = [sorted_contestants[-1], sorted_contestants[-2]]

        if len(episode.contestants) == 4:
            test = 1
        lipsync = episode.lipsync(episode.bottom2[0], episode.bottom2[1])
        eliminated = lipsync[1]
        test = 0

        # Remove the eliminated contestant from the current contestants
        self.current_contestants.remove(eliminated)

        # Add episode to the season's episodes list
        self.add_episode(episode)

        return episode

    def simulate_finale(self, challenge):
        """Simulates the finale episode of the season."""
        episode = Episode(len(self.episodes) + 1, self.current_contestants, challenge)
        for contestant in self.current_contestants:
            episode.scores[contestant] = contestant.perform_challenge(challenge)
        winner = episode.determine_winner()
        return [winner, episode]

    def _simulate_regular_episodes(self):
        """Simulates all regular episodes until reaching the finale."""
        # Simulate each episode until the number of current_contestants matches the finale type
        while len(self.current_contestants) > self.finale_type:
            # Placeholder challenge for now
            challenge = Challenge(len(self.challenges) + 1, "Test Challenge", *[1 for _ in range(12)])
            self.challenges.append(challenge)
            # Simulate the episode
            self.simulate_episode(challenge)

    def _simulate_finale_episode(self):
        """Simulates the finale episode of the season."""
        # Placeholder challenge for now
        challenge = Challenge(len(self.challenges) + 1, "Finale Challenge", *[1 for _ in range(12)])
        self.challenges.append(challenge)
        # Simulate the finale
        self.simulate_finale(challenge)

    def run_season(self):
        """Simulates the entire season from start to finish."""
        self._simulate_regular_episodes()
        self._simulate_finale_episode()

        # Determine the winner
        winner = finale_list[0]
        winner_ep = finale_list[1]
        a = 1

        return winner

    def get_winner(self, finale_episode):
        """Returns the winner of the season after all episodes are simulated."""
        # Placeholder logic to get the season winner (e.g., highest score in the finale)
        # This can be expanded based on specific criteria
        test = 1
        return finale_episode.winners[0]

    def set_finale_type(self, type):
        """Sets the type of finale (Top 3 or Top 4)."""
        self.finale_type = type

    # Additional methods can be added as needed.

# This is a basic draft of the Season class. Further refinement and additions can be made based on requirements.

import config
from challenge import Challenge
from contestant import Contestant
from episode import Episode
from season import Season

# Initialize a mock season with mock contestants
mock_contestants = [Contestant(name=f"Contestant {i}", stats={col: 5 for col in config.DB_COLUMNS[1:]}) for i in range(1, 13)]
mock_season = Season(id=1, contestants=mock_contestants, finale_type=3)
mock_season.run_season()

breakpoint_test = 1
# Test the run_season method
season_winner = mock_season.run_season()
print(f"Winner of the season: {season_winner.name}")  # Should print the contestant with the highest overall score

# Test the get_winner method
mock_finale_challenge = Challenge(3, "Mock Finale Challenge", *([1] * (len(config.DB_COLUMNS) - 1)))
mock_finale_episode = Episode(3, mock_season.current_contestants, mock_finale_challenge)
finale_winner = mock_season.get_winner(mock_finale_episode)
print(f"Winner of the finale: {finale_winner.name}")  # Should print the contestant with the highest score in the finale

# Test the set_finale_type method
mock_season.set_finale_type(4)
print(f"Updated finale type: {mock_season.finale_type}")  # Should print 4

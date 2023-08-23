# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from episode import Episode
from contestant import Contestant
from challenge import Challenge
import config
import random
# Assume you have the necessary classes and functions defined

def create_test_episode():
    # Create contestants with names and randomized stats
    contestant_data = [
        {
            "name": "Contestant " + str(i),
            "stats": [random.randint(1, 10) for _ in range(len(config.DB_COLUMNS) - 1)]
        }
        for i in range(1, 15)
    ]
    contestants = [Contestant(**data) for data in contestant_data]



    # Simulate challenge scores for each contestant
    challenge = Challenge(1, "Test Challenge", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    # Create an episode
    episode = Episode(1,contestants,challenge)

    for contestant in contestants:
        episode.scores[contestant] = contestant.perform_challenge(challenge)

    # Categorize contestants into groups
    episode.categorize_contestants()

    return episode





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Set the random seed for reproducibility
    random.seed(config.RANDOM_SEED)  # Replace 42 with your desired seed value

    # Create a test episode
    test_episode = create_test_episode()

    print("HIGH Group:")
    for contestant in test_episode.high_group:
        print(contestant.name, "-", test_episode.scores[contestant])

    print("\nSAFE Group:")
    for contestant in test_episode.safe_group:
        print(contestant.name, "-", test_episode.scores[contestant])

    print("\nLOW Group:")
    for contestant in test_episode.low_group:
        print(contestant.name, "-", test_episode.scores[contestant])

    test = 1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

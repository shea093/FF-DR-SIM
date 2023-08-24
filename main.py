# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from episode import Episode
from contestant import Contestant
from challenge import Challenge
import config
import random
import json
import season
# Assume you have the necessary classes and functions defined


def load_challenges_from_json(json_path):
    """
    Load challenge data from a JSON file and create Challenge objects.

    :param json_path: Path to the JSON file containing challenge data.
    :return: List of Challenge objects.
    """
    with open(json_path, "r") as file:
        challenge_data = json.load(file)

    challenge_objects = []
    for data in challenge_data:
        name = data["name"]
        biases = [data["biases"][stat] for stat in config.DB_COLUMNS[1:]]
        challenge_objects.append(Challenge(name, *biases))

    return challenge_objects


def load_objects_from_json(json_path, object_class, attributes_mapping):
    """
    Load data from a JSON file and create objects based on a provided class structure.

    :param json_path: Path to the JSON file containing data.
    :param object_class: The class to create objects from.
    :param attributes_mapping: A dictionary mapping attribute names to keys in the JSON data.
    :return: List of objects created from the JSON data.
    """
    with open(json_path, "r") as file:
        data = json.load(file)

    objects = []
    for item in data:
        attributes = [item[key] for key in attributes_mapping.values()]
        objects.append(object_class(*attributes))
        if object_class is Contestant:
            test = 1
        # debug


    return objects


def load_contestants_from_json(json_path):
    """
    Load contestant data from a JSON file and create Contestant objects.

    :param json_path: Path to the JSON file containing contestant data.
    :return: List of Contestant objects.
    """
    with open(json_path, "r") as file:
        contestant_data = json.load(file)

    contestant_objects = []
    for data in contestant_data:
        name = data["name"]
        stats = data["stats"]
        test = 1
        contestant_objects.append(Contestant(name, stats))

    return contestant_objects


def create_test_episode():
    # Create contestants with names and randomized stats
    contestant_data = [
        {
            "name": "Contestant " + str(i),
            "stats": [random.randint(1, 10) for _ in range(len(config.DB_COLUMNS) - 1)]
        }
        for i in range(1, 14)
    ]
    contestants = [Contestant(**data) for data in contestant_data]



    # Simulate challenge scores for each contestant
    challenge = Challenge(1, "Test Challenge", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    test_challenges = load_objects_from_json("json_data/rpdr_challenges.json", Challenge, {"name": "name", "biases": "biases"})
    test_contestants = load_contestants_from_json("json_data/final_ffxiv_contestants_extended.json")

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

    # Determine winners
    winners = test_episode.determine_winner()
    bottom2 = test_episode.determine_bottom_2()


    # Display results
    print("Episode Results:")
    print("Contestants:")
    for contestant in test_episode.contestants:
        print(contestant)

    print("\nCategorized Groups:")
    print("HIGH Group:", [contestant.name for contestant in test_episode.high_group])
    print("LOW Group:", [contestant.name for contestant in test_episode.low_group])
    print("SAFE Group:", [contestant.name for contestant in test_episode.safe_group])

    print("\nWinners:")
    for winner in winners:
        print(winner.name)

    print("\nBottom 2:")
    for btm in bottom2:
        print(btm.name)

    test = 1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

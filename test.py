import config
from challenge import Challenge
from contestant import Contestant
from episode import Episode
from season import Season
import config
import random
import json

random.seed(config.DOUBLE_WINNER_CHANCE)
# Initialize a mock season with mock contestants
# Generate random floating point stats between 0 and 10
def generate_random_stats():
    return [round(random.uniform(0, 10), 2) for _ in range(11)]

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

# List of names (feel free to replace with real ones if you have any preference)
names = [
    "Alex", "Blake", "Charlie", "Dana", "Eli",
    "Fran", "Grace", "Harley", "Ivy", "Jamie",
    "Kris", "Lou", "Morgan", "Nicky", "Ollie"
]

# Generate Contestants
# mock_contestants = [Contestant(name, *generate_random_stats()) for name in names]
test_challenges = load_objects_from_json("json_data/rpdr_challenges.json", Challenge,
                                         {"name": "name", "biases": "biases"})
mock_contestants = load_objects_from_json("json_data/ffxiv_2.json", Contestant, {"name": "name", "stats": "stats"})
test

mock_season = Season(id=1, contestants=mock_contestants, finale_type=3)
season_winner = mock_season.run_season()


# Test the run_season method
print(f"Winner of the season: {season_winner}")  # Should print the contestant with the highest overall score



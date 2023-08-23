import config

class Challenge:
    _DB_COLUMNS = config.DB_COLUMNS
    def __init__(self, id, name, *biases):
        """
        Initialize a Challenge object with specified attributes and biases.

        :param id: The ID of the challenge.
        :param name: The name of the challenge.
        :param biases: Bias values for each attribute, ordered according to DB_COLUMNS.
        """
        self.id = id
        self.name = name
        self.biases = dict(zip(config.DB_COLUMNS[1:], biases))


    def simulate_challenge(self, contestant):
        """
        Simulate the performance of the challenge for a given contestant.

        :param contestant: The Contestant object performing the challenge.
        :return: A simulated challenge score based on contestant attributes and biases.
        """
        total_bias = sum(self.biases.values())

        # Calculate challenge score based on biases and contestant stats
        challenge_score = sum(
            (self.biases[attr] * getattr(contestant, attr))
            for attr in self.biases
        ) / total_bias * 100

        return challenge_score
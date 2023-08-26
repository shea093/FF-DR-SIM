import config

class Challenge:
    _DB_COLUMNS = config.DB_COLUMNS
    def __init__(self, id, name, biases):
        """
        Initialize a Challenge object with specified attributes and biases.

        :param id: The ID of the challenge.
        :param name: The name of the challenge.
        :param biases: Bias values for each attribute, ordered according to DB_COLUMNS.
        """
        self.id = id
        self.name = name
        self.biases = biases

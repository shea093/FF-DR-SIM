import sqlite3

class Challenge:
    def __init__(self, id, name, charisma_bias, creativity_bias, runway_presence_bias,
                 performance_skills_bias, sewing_and_crafting_bias, comedy_bias,
                 drama_and_emotion_bias, adaptability_bias, teamwork_bias,
                 confidence_bias, lipsyncing_bias):
        self.id = id
        self.name = name
        self.biases = {
            "charisma": charisma_bias,
            "creativity": creativity_bias,
            "runway_presence": runway_presence_bias,
            "performance_skills": performance_skills_bias,
            "sewing_and_crafting": sewing_and_crafting_bias,
            "comedy": comedy_bias,
            "drama_and_emotion": drama_and_emotion_bias,
            "adaptability": adaptability_bias,
            "teamwork": teamwork_bias,
            "confidence": confidence_bias,
            "lipsyncing": lipsyncing_bias
        }

    def simulate_challenge(self, contestant):
        total_bias = sum(self.biases.values())

        # Calculate challenge score based on biases and contestant stats
        challenge_score = sum(
            (self.biases[attr] * getattr(contestant, attr))
            for attr in self.biases
        ) / total_bias * 100

        return challenge_score

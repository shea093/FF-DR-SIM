import sqlite3
import random

# Define the Contestant class
class Contestant:
    def __init__(self, id, name, charisma, creativity, runway_presence, performance_skills,
                 sewing_and_crafting, comedy, drama_and_emotion, adaptability,
                 teamwork, confidence, lipsyncing):
        self.id = id
        self.name = name
        self.charisma = charisma
        self.creativity = creativity
        self.runway_presence = runway_presence
        self.performance_skills = performance_skills
        self.sewing_and_crafting = sewing_and_crafting
        self.comedy = comedy
        self.drama_and_emotion = drama_and_emotion
        self.adaptability = adaptability
        self.teamwork = teamwork
        self.confidence = confidence
        self.lipsyncing = lipsyncing
        self.score = 0  # Initialize score to 0

    def insert_into_db(self):
        conn = sqlite3.connect('ff_dr_sim.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO contestants (
                name, charisma, creativity, runway_presence, performance_skills,
                sewing_and_crafting, comedy, drama_and_emotion, adaptability,
                teamwork, confidence, lipsyncing
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            self.name,
            self.charisma,
            self.creativity,
            self.runway_presence,
            self.performance_skills,
            self.sewing_and_crafting,
            self.comedy,
            self.drama_and_emotion,
            self.adaptability,
            self.teamwork,
            self.confidence,
            self.lipsyncing
        ))

        conn.commit()
        conn.close()

# Define the Episode class
class Episode:
    def __init__(self, id, episode_number):
        self.id = id
        self.episode_number = episode_number

    def insert_into_db(self):
        conn = sqlite3.connect('ff_dr_sim.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO episodes (episode_number)
            VALUES (?)
        ''', (self.episode_number,))

        conn.commit()
        conn.close()

# Create tables if they don't exist
def create_tables():
    conn = sqlite3.connect('ff_dr_sim.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contestants (
        CREATE TABLE IF NOT EXISTS contestants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        charisma INTEGER,
        creativity INTEGER,
        runway_presence INTEGER,
        performance_skills INTEGER,
        sewing_and_crafting INTEGER,
        comedy INTEGER,
        drama_and_emotion INTEGER,
        adaptability INTEGER,
        teamwork INTEGER,
        confidence INTEGER,
        lipsyncing INTEGER,
        score INTEGER DEFAULT 0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS episodes (
            id INTEGER PRIMARY KEY,
            episode_number INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# ... (rest of the code remains unchanged) ...

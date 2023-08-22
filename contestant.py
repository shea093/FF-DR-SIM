# contestant.py

import sqlite3

class Contestant:
    # Update when adding new attributes to __init__
    _DB_COLUMNS = ['name', 'charisma', 'creativity', 'runway_presence', 'performance_skills', 'sewing_and_crafting',
                   'comedy', 'drama_and_emotion', 'adaptability', 'teamwork', 'confidence', 'lipsyncing']

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
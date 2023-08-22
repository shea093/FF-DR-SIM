import sqlite3

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
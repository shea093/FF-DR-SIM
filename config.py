# config.py

# Randomness configuration
RANDOM_SEED = 5545  # Set the random seed for reproducibility
RANDOM_VARIABILITY = 0.1 # Set the percentage of random variability for episode scores
DB_COLUMNS = ['name', 'charisma', 'creativity', 'runway_presence', 'performance_skills', 'sewing_and_crafting',
               'comedy', 'drama_and_emotion', 'adaptability', 'teamwork', 'confidence', 'lipsyncing']
#Variable for setting % of a double win chance, use 1-100
DOUBLE_WINNER_CHANCE = 15

#VARIABILITY FOR LIPSYNCS
MIN_LIPSYNC = 0.4
MAX_LIPSYNC = 2
LIPSYNC_STAT_WEIGHT = 0.8  # Weight for the contestant's lip syncing stat

import math

def calculate_rpm(string):
    WORD_PER_MINUTE = 200
    if len(string) < 1:
        raise Exception("Can't estimate reading time for empty text")

    # 1. divide number of words with 200 to see how many minutes it will take => might return float
    # 2. since it can return float, we have to use math.ceil so eg. 1.2 becomes 2
    minutes = math.ceil(len(string.split()) / WORD_PER_MINUTE) 
    if minutes <= 1:
        return "1 minute"
    else:
        return f"{minutes} minutes"
    
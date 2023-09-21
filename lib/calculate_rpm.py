import math

def calculate_rpm(string):
    WORD_PER_MINUTE = 200

    minutes = math.ceil(len(string.split()) / WORD_PER_MINUTE)
    if minutes <= 1:
        return "1 minute"
    else:
        return f"{minutes} minutes"
    
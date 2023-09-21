def calculate_rpm(string):
    WORD_PER_MINUTE = 200
    
    words = len(string.split())
    if words <= 200:
        return "1 minute"
    else:
        return "2 minutes"
    
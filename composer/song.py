
class Song:
    TECHNO = "techno"

    styles = (
        TECHNO,
    )
    
    HAPPY = "happy"

    moods = (
        HAPPY,
    )

    def __init__(self):
        self.style = None
        self.mood = None
        self.arrangement = None

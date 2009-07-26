
class Note:

    # number is from 1-7
    def __init__(self, number, duration=1.0):
        self.number = number
        self.duration = duration

    def __str__(self):
        return str(self.number) + ":" + str(self.duration)

    def translate(self, offset):
        self.number += offset

    def getTranslation(self, offset):
        return Note(self.number + offset)


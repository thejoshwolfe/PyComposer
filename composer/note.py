
class Note:

    # number is from 1-7
    def __init__(self, number, duration=1.0, velocity=0x40):
        self.number = number
        self.duration = duration
        self.velocity = 0x40

    def __str__(self):
        return str(self.number) + ":" + str(self.duration)

    def translate(self, offset):
        self.number += offset

    def getTranslation(self, offset):
        return Note(self.number + offset, self.duration)

    def clone(self):
        return Note(self.number, self.duration, self.velocity)



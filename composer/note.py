
def normalize(number):
    return ((number - 1) % 7) + 1

class Note:

    # number is from 1-7
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def translate(self, offset):
        self.number += offset

    def getTranslation(self, offset):
        return Note(self.number+offset)


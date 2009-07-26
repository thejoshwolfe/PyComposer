
def normalize(number):
    return ((number - 1) % 7) + 1

class Note:

    # number is from 1-7
    def __init__(self, number):
        self.number = normalize(number)

    def __str__(self):
        return str(self.number)


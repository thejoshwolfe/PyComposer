from .note import Note

class Chord:
    def __init__(self, root):
        self.notes = [Note(root+i) for i in (0, 2, 4)]

    def __str__(self):
        return ",".join([str(x) for x in self.notes])


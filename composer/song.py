
major = [0, 2, 4, 5, 7, 9, 11]
minor = [0, 2, 3, 5, 7, 8, 10]

class Song:
    def __init__(self):
        self.tracks = []
        self.tempo = 140 # BPM
        self.beatsPerMeasure = 4
        self.key = 0x40
        self.mode = major
    
    def addTrack(self, track):
        self.tracks.append(track)
    
    def noteToPitch(self, note):
        """
        returns the midi pitch (int) for a note in the current key and mode
        """
        offsetIntoMode = ((note.number - 1) % 7) + 1
        octaveOffset = 12 * (offsetIntoMode - note.number) / 7
        return self.key + octaveOffset + self.mode[offsetIntoMode]
    
    def writeToMidi(self, filepath):
        raise(TODO) # :p



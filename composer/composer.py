from random import randint, random
from .chord import Chord
from .song import Song
from .note import Note

__name__ = 'PyComposer'
__version__ = '0.0.1'
__doc__ = 'Music composer bot written in Python 3'
__author__ = 'Josh Wolfe; Andrew Kelley'
__email__ = 'thejoshwolfe@gmail.com'

# this class will be the main class you import to do stuff

chord_structures = (
    [1, 4, 5, 5],
    [1, 4, 5, 1],
    [1, 4, 1, 5],
    [1, 2, 3, 4],
)
def chordGen():
    bones = chord_structures[randint(0, len(chord_structures)-1)]
    chords = []

    for root in bones:
        offset = randint(-1, 1) * 0
        chords.append(Chord(root+offset))

    return chords

# create a song from scratch
def compose():
    s = Song()

    # choose a style
    s.style = Song.styles[randint(0, len(Song.styles)-1)]

    # choose a mood
    s.mood = Song.moods[randint(0, len(Song.moods)-1)]

    # generate a song arrangement
    s.arrangement = genArrangement()
    

def genArrangement():
    output = []

    if randint(0,1) == 0:
        output = "VCVCBC"
    else:
        output = "CVCVBC"
    
    # mangle it
    if random() <= 0.90:
        # add intro
        output = "I" + output
    
    if random() <= 0.90:
        # add outro
        output += "O"

    return output


def createMelody(progression):
    def genRandomCrap(offset, size, chord, notes):
        # at each beat, pick a random note from the first chord and place it
        for i in range(offset, offset+size):
            index = randint(0,2)
            note = chord.notes[index]
            notes[i] = note
        
        # iterate through half beats, optionally adding more
        for i in range(offset, offset+size):
            if random() <= .30:
                if i == offset+size-1 or randint(0,1):
                    baseNote = notes[i]
                else:
                    baseNote = notes[i+1]

                newNote = baseNote.getTranslation((-2, -1, 0, 1, 2)[randint(0, 4)])
                notes[i+0.5] = newNote

    def copyBar(oldOff, size, oldChord, newChord, newPos, notes):
        offset = newChord.notes[0].number - oldChord.notes[0].number
        firstBarPos = filter(lambda x: x >= oldOff and x < oldOff+size,
            notes.keys())
        for pos in firstBarPos:
            notes[pos-oldOff+newPos] = notes[pos].getTranslation(offset)
        
    notes = {}
    
    # first bar is random
    genRandomCrap(0, 4, progression[0], notes)

    # create second bar based on the first
    copyBar(0, 4, progression[0], progression[1], 4, notes)

    # tension: do random stuff here
    genRandomCrap(8, 4, progression[2], notes)
    
    # last bar: each half has 3 options: copy 1st bar, copy 3rd bar, or random
    for i in range(2):
        what = randint(0, 2)
        print("i: %i what: %i" % (i, what))
        if what == 0:
            # copy 1st
            copyBar(i*2, 2, progression[0], progression[3], 12+i*2, notes)
        elif what == 1:
            # copy 3rd
            copyBar(8+i*2, 2, progression[2], progression[3], 12+i*2, notes)
        else:
            # random
            genRandomCrap(12+i*2, 2, progression[3], notes)

    # add a final note
    notes[16] = Note(8)

    
    return notes

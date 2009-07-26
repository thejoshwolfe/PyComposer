from random import randint
from .chord import Chord

__name__ = 'PyComposer'
__version__ = '0.0.1'
__doc__ = 'Music composer bot written in Python 3'
__author__ = 'Josh Wolfe; Andrew Kelley'
__email__ = 'thejoshwolfe@gmail.com'

# this class will be the main class you import to do stuff

chord_structures = (
    [1, 1, 4, 5],
    [1, 1, 5, 5],
    [1, 4, 5, 5],
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
    # choose a style

    # choose a mood

    # generate a song arrangement
    pass

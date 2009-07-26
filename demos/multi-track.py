# create a random melody into a midi using
# an acoustic grand piano

from midi.MidiOutFile import MidiOutFile
from composer import composer
import os

from composer.note import normalize

from random import randint

def putInScale(note):
    scale = (0, 2, 4, 5, 7, 9, 11)
    norm = normalize(note.number)
    return ((note.number - norm) / 7) * 12 + scale[norm-1]

def noteToMidi(note):
    return 0x43+putInScale(note)


def addChord(chord):
    for note in chord.notes:
        midi.update_time(0)
        midi.note_on(channel=1, note=noteToMidi(note), velocity=0x20)

    rel = 4
    midiTime = int(float(rel) / 16.0 * 192.0*8.0*2)
    midi.update_time(midiTime)
    for note in chord.notes:
        midi.note_off(channel=1, note=noteToMidi(note))
        midi.update_time(0)

# grab a chord progression
progression = composer.chordGen()
print("progression:")
for chord in progression:
    print(str(chord))

# render a melody
melody = composer.createMelody(progression)


out_file = 'out.mid'

midi = MidiOutFile(out_file)

midi.header(1, 2, 480)


midi.start_of_track(0)
midi.tempo(750000)
midi.time_signature(4, 2, 24, 8)

midi.patch_change(0, 57)

positions = melody.keys()
positions.sort()
print("melody:")
lastPos = 0
for pos in positions:

    rel = pos - lastPos
    midiTime = int(float(rel) / 16.0 * 192.0*8.0*2)

    output = "\n" * int(rel * 2 - 1)
    output += "%so" % str(" " * (melody[pos].number+7))
    print(output)
    
    #print("pos: %s note: %s midi: %s" % (str(pos), str(melody[pos]), str(midiTime)))
    midi.update_time(midiTime)
    midi.note_on(channel=0, note=noteToMidi(melody[pos]))

    rel = 0.5
    midiTime = int(float(rel) / 16.0 * 192.0*8.0*2)
    midi.update_time(midiTime)
    midi.note_off(channel=0, note=noteToMidi(melody[pos]))

    lastPos = pos + rel


    
midi.update_time(0)
midi.end_of_track()

midi.start_of_track(1)
midi.tempo(750000)
midi.time_signature(4, 2, 24, 8)

midi.patch_change(1, 75)

for chord in progression:
    addChord(chord)
midi.end_of_track()

midi.eof() # currently optional, should it do the write instead of write??


os.system('timidity %s' % out_file)


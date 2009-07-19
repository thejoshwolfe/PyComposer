
import sys
sys.path.append("code")
from imports import *



chords = list(data.chords.values())
chords.sort(key=lambda chord: chord.name)

for chord in chords:
	print(chord)




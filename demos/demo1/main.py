
import random
from functools import reduce

from composer.chords import chords

# make a random 4-bar chord progression

progression = []
for _ in range(4):
	progression.append(list(chords.values())[random.randint(0,len(chords)-1)])

# end with a 1 chord
progression.append(chords["1"])


# print to console
print("random chord progression:")
print()
print("chord\ttension")
for c in progression:
	print(c.name + "\t" + c.tension * "*")
print("total tension: " + str(reduce(lambda acc, c: acc + c.tension, progression, 0)))



## print the list of chords
#chords = list(chords.values())
#chords.sort(key=lambda chord: chord.name)
#for chord in chords:
#	print(chord)




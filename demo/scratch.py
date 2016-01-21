# http://stackoverflow.com/questions/10983462/how-can-i-produce-real-time-audio-output-from-music-made-with-music21
#
#  Set up a detuned piano
#  (where each key has a random
#  but consistent detuning from 30 cents flat to sharp)
#  and play a Bach Chorale on it in real time.

from music21 import *
import random
keyDetune = []
for i in range(0, 127):
    keyDetune.append(random.randint(-30, 30))

b = corpus.parse('bach/bwv66.6')
for n in b.flat.notes:
    n.microtone = keyDetune[n.midi]
sp = midi.realtime.StreamPlayer(b)
sp.play()
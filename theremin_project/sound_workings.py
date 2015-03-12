""" Synthesizes a blues solo algorithmically """

from Nsound import *
import numpy as np
from random import choice
import time
import pygame
pygame.init()



def add_note(out, instr, key_num, duration, bpm, volume):
    """ Adds a note from the given instrument to the specified stream

    out: the stream to add the note to
    instr: the instrument that should play the note
    key_num: the piano key number (A 440Hzz is 49)
    duration: the duration of the note in beats
    bpm: the tempo of the music
    volume: the volume of the note
    """
    freq = (2.0**(1/12.0))**(int(key_num)-49)*440.0
    stream = instr.play(duration*(60.0/bpm),freq)
    stream *= volume
    out << stream

def playanote(keygiven, volumegiven):

    # this controls the sample rate for the sound file you will generate
    sampling_rate = 44100.0
    Wavefile.setDefaults(sampling_rate, 16)

    organ = OrganPipe(sampling_rate)	# use an organ as the instrument
    solo = AudioStream(sampling_rate, 1)

    """ these are the piano key numbers for a 3 octave blues scale in A
    	See: http://en.wikipedia.org/wiki/Blues_scale """
    blues_scale = [25, 28, 30, 31, 32, 35, 37, 40, 42, 43, 44, 47, 49, 52, 54, 55, 56, 59, 61]
    beats_per_minute = 45				# Let's make a slow blues solo

    add_note(solo, organ ,blues_scale[keygiven], 3, beats_per_minute, volumegiven)

    solo >> "blues_solo.wav"

    pygame.mixer.music.load("blues_solo.wav")
    pygame.mixer.music.play()

playanote(3, 1)
time.sleep(10)
#playanote(6, 2)
#playanote(2, 1)
#playanote(3, 1)
# playanote(6, 2)
# playanote(2, 1)
# playanote(3, 1)
# playanote(6, 2)
# playanote(2, 1)
# playanote(3, 1)
# playanote(6, 2)
# playanote(2, 1)
import numpy
import pandas
from random import randint
from Emotional_Responses import insult, compliment, flirty, sad
from emotion import Emotion
from wnaffect import WNAffect
import nltk

def main():
    wna = WNAffect('wordnet-1.6/','wn-domains-3.2/')
    word = ['annoyance']
    pos= nltk.pos_tag(word)
    emo = wna.get_emotion(pos[0][0],pos[0][1])
    print(pos)
    print(pos[0][0])
    print(pos[0][1])
    print(emo)
main()

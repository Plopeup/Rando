import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from Emotional_Responses import insult, compliment, flirty, sad
from spellchecker import SpellChecker
from Sentiment import get_phrase_sentiment as gps, clean_phrase as cp
from Analysis import neutral_analysis, Emotion

def main():
    x=0
    sad_response =[]
    happy_response =[]
    anger_response=[]
    flirt_response=[]
    neutral_response=[]
    print("Hello, I am Rando\n")
    while x!=1:
        sayin = input()
        a=(cp(sayin))
        a=a.split(' ')
        return(Emotion(a,gps(sayin)))


print(main())

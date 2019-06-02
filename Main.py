import numpy
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from random import randint
from Emotional_Responses import insult, compliment, flirty, sad
import nltk
from textblob import TextBlob
from spellchecker import SpellChecker
from sentiment import get_phrase_sentiment as gps

def main():
    x=0
    df = pd.read_excel('Rando-Database.xlsx')
    sad = df['Sad']
    flirt = df['Flirtatious']
    happy = df['Happy']
    anger = df['Anger']
    sad_response =[]
    happy_response =[]
    anger_response=[]
    flirt_response=[]
    neutral_response=[]
    print("Hello, I am Rando\n")
    while x!=1:
        sayin = input()
        print(gps(sayin))
        x=1

main()

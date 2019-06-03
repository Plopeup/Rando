import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from Emotional_Responses import insult, compliment, flirty, sad
from spellchecker import SpellChecker
from Sentiment import get_phrase_sentiment as gps, clean_phrase as cp

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
        a=(cp(sayin))
        a=a.split(' ')
        print(a)
        if gps == 'neutral':
            while y!=1:
                support = input(("I apologize how should I feel? Postive/Negative/Neutral \n"))
                support_choice=['positive','negative', 'neutral']
                negative_choice = ['negative','n']
                if lower(support) == 'negative':
                    print('Please input one of the answers given\n')
                #else:
                    #if lower(support) in negative_choice:

        x=1

main()

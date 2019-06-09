import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from Emotional_Responses import insult, compliment, flirty, sad
from Sentiment import get_phrase_sentiment as gps, clean_phrase as cp
from Analysis import neutral_analysis, Emotion, emotion_to_excel

def main():
    x=0
    new_happy, new_sad, new_flirt, new_anger = [], [], [], []
    sad_response, happy_response, anger_response, flirt_response = [], [], [], []
    total_sad, total_happy, total_anger, total_flirt, spectrum = 0, 0, 0, 0, 0
    print("Hello, I am Rando\n")
    while x!=1:
        sayin = input("Input: ")
        sayin_list = cp(sayin).split(' ')
        emotion_dic = Emotion(sayin_list,gps(sayin))
        if emotion_dic['Feeling'] == 'positive':
            happy_points, flirt_points = 0, 0
            happy_points += emotion_dic['Happy Points']
            flirt_points += emotion_dic['Flirt Points']
            spectrum += happy_points + flirt_points
            if flirt_points > happy_points:
                if spectrum < 0:
                    print("Rando: "+flirty(0))
                else:
                    flirt_response.append(sayin)
                    total_flirt += flirt_points
                    print("Rando: "+flirty(total_flirt))
            if happy_points >= flirt_points:
                if spectrum < 0:
                    print("Rando: "+compliment(0))
                else:
                    happy_response.append(sayin)
                    total_happy += happy_points
                    print("Rando: "+compliment(total_happy))
        elif emotion_dic['Feeling'] == 'negative':
            sad_points, anger_points = 0, 0
            sad_points += emotion_dic['Sad Points']
            anger_points += emotion_dic['Anger Points']
            spectrum -= sad_points + anger_points
            print(spectrum)
            if anger_points > sad_points:
                if spectrum > 0:
                    print("Rando: "+ insult(0))
                else:
                    anger_response.append(sayin)
                    total_anger += anger_points
                    print("Rando: "+ insult(total_anger))
            if sad_points >= anger_points:
                if spectrum > 0:
                    print("Rando: "+ sad(0))
                else:
                    sad_response.append(sayin)
                    total_sad += sad_points
                    print("Rando: "+ sad(total_sad))
        else:
            neutral_change = neutral_analysis(sayin)
            if neutral_change != None:
                for i in neutral_change:
                    if i[1] == 'Happy':
                        new_happy.append(i[0])
                    if i[1] == 'Anger':
                        new_anger.append(i[0])
                    if i[1] == 'Sadness':
                        new_sad.append(i[0])
                    if i[1] == 'Flirtatious':
                        new_flirt.append(i[0])
                    emotion_to_excel(new_sad,new_happy,new_anger,new_flirt)
                print(new_happy)
                print(new_anger)
                print(new_sad)
                print(new_flirt)
main()

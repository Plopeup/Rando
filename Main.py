import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from Emotional_Responses import insult, compliment, flirty, sad
from Sentiment import get_phrase_sentiment as gps, clean_phrase as cp
from Analysis import neutral_analysis, Emotion, emotion_to_excel

def main():
    x=0
    #These new_statements will save new words that AI did not think of yet
    new_happy, new_sad, new_flirt, new_anger = [], [], [], []
    #These emotion_response is lists where we store every response from the user
    sad_response, happy_response, anger_response, flirt_response = [], [], [], []
    #These Total_emotion and spectrum will be used to deterimne the mood of Rando
    total_sad, total_happy, total_anger, total_flirt, spectrum = 0, 0, 0, 0, 0
    print("Hello, I am Rando\n")
    #The whole chat is done in this while loop
    while x!=1:
        sayin = input("Input: ")
        #sayin_list turns the statement into a list of words so we can analyze it
        sayin_list = cp(sayin).split(' ')
        #emotion_dic will return a dictionary with the type of feeling and and emotion
        emotion_dic = Emotion(sayin_list,gps(sayin))
        #Here we calculate which emotions will be shown from the statement by transcribing them to points
        if emotion_dic['Feeling'] == 'positive':
            happy_points, flirt_points = 0, 0
            happy_points += emotion_dic['Happy Points']
            flirt_points += emotion_dic['Flirt Points']
            #spectrum will show us the mood of the AI >0 is positive <0 is negative
            spectrum += happy_points + flirt_points
            #depending on the spectrum it will decide which emotional response to give
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
        #This is the same as the last one but with negative feeling
        elif emotion_dic['Feeling'] == 'negative':
            sad_points, anger_points = 0, 0
            sad_points += emotion_dic['Sad Points']
            anger_points += emotion_dic['Anger Points']
            spectrum -= sad_points + anger_points
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
            #if there is neutral we will ask how the AI should feel from the statement
            #Then will append the word with the emotional impact to the correct new_emotion list
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
                    #emotion_to_excel will update the database
                    emotion_to_excel(new_sad,new_happy,new_anger,new_flirt)
main()

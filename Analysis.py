import pandas as pd
from Sentiment import stop_word_removal as SWR, clean_phrase as CP

#If the feeling is neutral then we will have to do a neutral analysis to make sure
def neutral_analysis(phrase):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    y=0
    x=0
    z=0
    edit = []
    while y!=1:
        support = input(("I apologize how should I feel? Postive/Negative/Neutral \n"))
        support_choice=['positive','negative', 'neutral']
        if support.lower() not in support_choice:
            print('Please input one of the answers given\n')
        if support.lower() == 'negative':
            word_choice = SWR(phrase)
            options = ''
            for i in range(len(word_choice)):
                options += "({}):'{}' ".format(i,word_choice[i])
            while x!=1:
                print("Please put the corresponding number to the words that have an emotional reaction\n")
                print("If there is multiple answers please seperate them with a space such as 0 2\n")
                print("If there is no emotional words enter n\n")
                support_words = input("{}\n".format(options))
                if hasNumbers(support_words) == False and support_words.lower() != 'n':
                    print("Please input a correct response\n")
                if hasNumbers(support_words) == True:
                    support_answers = CP(support_words).split(' ')
                    print(support_answers)
                    answer_number = (list(range(len(word_choice))))
                    if valid_answer(support_answers, list(range(len(word_choice)))) == False:
                        print("Please input a correct response\n")
                    else:
                        for i in support_answers:
                            z=0
                            while z!=1:
                                print("What does emotion does this word '{}' spark?\n".format(word_choice[int(i)]))
                                feels = input("(A):Anger (B):Sadness (C):Flirt (D):Happy\n")
                                Emo_Dic = {'A':'Anger','B':'Sadness','C':'Flirtatious','D':'Happy'}
                                feels_choice = ['a','b','c','d']
                                if feels.lower() not in feels_choice:
                                    print("Please input a correct response\n")
                                else:
                                    a = word_choice[int(i)]
                                    b = feels.upper()
                                    b = (Emo_Dic[b])
                                    edit.append((a, b))
                                    z=1
                        return(edit)

#Determines Emotion Points as well as a positive or negatvie feeling
def Emotion(phrase_list, sentiment):
    df = pd.read_excel('Rando-Database.xlsx')
    sad = df['Sad'].tolist()
    flirt = df['Flirtatious'].tolist()
    happy = df['Happy'].tolist()
    anger = df['Anger'].tolist()
    sad_point=0
    happy_point=0
    angry_point=0
    flirt_point=0
    for i in phrase_list:
        if i.lower() in sad:
            sad_point+=1
        if i.lower() in happy:
            happy_point+=1
        if i.lower() in anger:
            angry_point+=1
        if i.lower() in flirt:
            flirt_point+=1
    negative_feeling = sad_point+angry_point
    positive_feeling = happy_point+flirt_point
    if sentiment == "positive":
        if negative_feeling >= 3 and positive_feeling == 0:
            return {'Feeling':'negative','Sad Points':sad_point,'Anger Points':angry_point}
        else:
            if positive_feeling == 0:
                happy_point+=1
            return {'Feeling':'positive','Happy Points':happy_point,'Flirt Points':flirt_point}
    if sentiment == "neutral":
        if negative_feeling > positive_feeling:
            return {'Feeling':'negative','Sad Points':sad_point,'Anger Points':angry_point}
        if negative_feeling == positive_feeling:
            return {'Feeling':'neutral'}
        else:
            return {'Feeling':'positive','Happy Points':happy_point,'Flirt Points':flirt_point}
    if sentiment == 'negative':
        if positive_feeling >= 3 and negative_feeling == 0:
            return {'Feeling':'positive','Happy Points':happy_point,'Flirt Points':flirt_point}
        else:
            if negative_feeling == 0:
                sad_point+=1
            return {'Feeling':'negative','Sad Points':sad_point,'Anger Points':angry_point}

#checks if the list has numbers in a list
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#checks if anything from one list is outside of another list
def valid_answer(inputList, checkList):
    try:
        for i in inputList:
            if int(i) not in checkList:
                return False
        return True
    except:
        print("Wrong Format, please input correctly\n")
        return False

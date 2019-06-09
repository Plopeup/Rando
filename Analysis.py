import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from Sentiment import stop_word_removal as SWR, clean_phrase as CP

#If the feeling is neutral then we will have to do a neutral analysis to make sure
def neutral_analysis(phrase):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    x, y, z, edit = 0, 0, 0, []
    while y!=1:
        support = input(("I apologize how should I feel? Positive/Negative/Neutral \n"))
        support_choice=['positive','negative', 'neutral']
        #this if statement will make sure the user inputted a valid response
        if support.lower() not in support_choice:
            print('Please input one of the answers given\n')
        #if the user chooses an emotion we will start to figure out which words spark which emotion
        if support.lower() == 'negative' or support.lower() == 'positive':
            #we are removing stop words from the phrase by using SWR
            word_choice = SWR(phrase)
            #we are creating options for the user, by creating a string options
            options = ''
            #this for loop will create a string with each word in the word_choice and give it a corresponding number alongside each word
            for i in range(len(word_choice)):
                options += "({}):'{}' ".format(i,word_choice[i])
            #This will ask the user to pick the words that have an emotional impact
            while x!=1:
                print("Please put the corresponding number to the words that have an emotional reaction\n")
                print("If there is multiple answers please seperate them with a space such as 0 2\n")
                print("If there is no emotional words enter n\n")
                #support words is the numbers corresponding to the words the user chose
                support_words = input("{}\n".format(options))
                #this will check if they put an invalid answer, no numbers or no n
                if hasNumbers(support_words) == False and support_words.lower() != 'n':
                    print("Please input a correct response\n")
                if hasNumbers(support_words) == True:
                    #CP will clear any excess characters that might be out of place
                    support_answers = CP(support_words).split(' ')
                    answer_number = (list(range(len(word_choice))))
                    #valid answer checks if it is a vald answer
                    if valid_answer(support_answers, list(range(len(word_choice)))) == False:
                        print("Please input a correct response\n")
                    else:
                        for i in support_answers:
                            z=0
                            #here we get the user to decide which emotion the words they chose spark
                            while z!=1:
                                print("What does emotion does this word '{}' spark?\n".format(word_choice[int(i)]))
                                feels = input("(A):Anger (B):Sadness (C):Flirt (D):Happy\n")
                                Emo_Dic = {'A':'Anger','B':'Sadness','C':'Flirtatious','D':'Happy'}
                                feels_choice = ['a','b','c','d']
                                if feels.lower() not in feels_choice:
                                    print("Please input a correct response\n")
                                # Once they choose then we pair the word with the emotion and return it as a tuple
                                else:
                                    a = word_choice[int(i)]
                                    b = feels.upper()
                                    b = (Emo_Dic[b])
                                    edit.append((a, b))
                                    z=1
                        return(edit)
                else:
                    return(None)
        if support.lower() == 'neutral':
            return(None)

#Determines Emotion Points as well as a positive or negatvie feeling, return a dictionary with feelings and emotional points
def Emotion(phrase_list, sentiment):
    df = pd.read_excel('Rando-Database.xlsx')
    #this will save the emotion words from the databse to a list that represents the same emotion
    sad = df['Sad'].tolist()
    flirt =  df['Flirtatious'].tolist()
    happy = df['Happy'].tolist()
    anger = df['Anger'].tolist()
    #these points will determine the phrases emotional output
    sad_point, happy_point, angry_point, flirt_point = 0, 0, 0, 0
    #we will check if any words from the phrase has any emotion based off the Rando databse
    for i in phrase_list:
        if i.lower() in sad:
            sad_point+=1
        if i.lower() in happy:
            happy_point+=1
        if i.lower() in anger:
            angry_point+=1
        if i.lower() in flirt:
            flirt_point+=1
    #negative and positive feeling is the sum of points from its similar feelings
    negative_feeling, positive_feeling = sad_point+angry_point, happy_point+flirt_point
    #we will determine the feeling by combining the sentiment given and the words used
    if sentiment == "positive":
        #if there are a lot fo negative points we will cahnge the feeling to negative
        if negative_feeling >= 3 and positive_feeling == 0:
            return {'Feeling':'negative','Sad Points':sad_point,'Anger Points':angry_point}
        else:
            #if there is no words matching any emotion but sentiment is positive it will be counted as happy by default
            if positive_feeling == 0:
                happy_point+=1
            return {'Feeling':'positive','Happy Points':happy_point,'Flirt Points':flirt_point}
    #if sentiment is neutral we will depend on word choice to make the decision
    if sentiment == "neutral":
        if negative_feeling > positive_feeling:
            return {'Feeling':'negative','Sad Points':sad_point,'Anger Points':angry_point}
        #if there is no one clear answer we will remain the statement as neutral
        if negative_feeling == positive_feeling:
            return {'Feeling':'neutral'}
        else:
            return {'Feeling':'positive','Happy Points':happy_point,'Flirt Points':flirt_point}
    #Samething as positive, we will use sentiment and word choice to determine a specific emotion
    if sentiment == 'negative':
        #if positive feeling is greater than negative then we will alter it to positive
        if positive_feeling >= 3 and negative_feeling == 0:
            return {'Feeling':'positive','Happy Points':happy_point,'Flirt Points':flirt_point}
        else:
            #if no word choice is selected then we will make it sad by default
            if negative_feeling == 0:
                sad_point+=1
            return {'Feeling':'negative','Sad Points':sad_point,'Anger Points':angry_point}

#adds the emotion words to the Database
def emotion_to_excel(sad_list,happy_list,angry_list,flirt_list):
    #we are saving the emotions word from the database to a list representing that emotion
    df = pd.read_excel('Rando-Database.xlsx')
    sad = df['Sad'].tolist()
    flirt = df['Flirtatious'].tolist()
    happy = df['Happy'].tolist()
    anger = df['Anger'].tolist()
    #we are going to merge the lists that are given to the list from the databse so we can rewrite a bigger list in the database
    #these statements are going to combine the new and old emotion list will removing any duplicate words
    sad = [x for x in sad if str(x) != 'nan']
    sad = list(set().union(sad,sad_list))
    flirt = [x for x in flirt if str(x) != 'nan']
    flirt = list(set().union(flirt, flirt_list))
    happy = [x for x in happy if str(x) != 'nan']
    happy = list(set().union(happy, happy_list))
    anger = [x for x in anger if str(x) != 'nan']
    anger = list(set().union(anger, angry_list))
    #we created a dictionary so we can enter the data into an excel sheet
    data_dict = {'Sad':sad, 'Happy':happy, 'Flirtatious':flirt, 'Anger':anger}
    #now we are creating a dataframe by the index side
    df1 = pd.DataFrame.from_dict(data_dict, orient='index')
    #now transpose will change the dataframe from row to columns
    df1 = df1.transpose()
    #This will overwrite the file with the new words list
    df1.to_excel("Rando-Database.xlsx")
    return


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

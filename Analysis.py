from Sentiment import stop_word_removal as SWR, clean_phrase as CP
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
                                    print(i)
                                    print(word_choice[int(i)])
                                    a = feels.upper()
                                    a = (Emo_Dic[a])
                                    edit = edit.append((word_choice[int(i)], a))
                                    print(edit)
                                    z=1
                                    print"stupid
                        return




def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def valid_answer(inputList, checkList):
    try:
        for i in inputList:
            if int(i) not in checkList:
                return False
        return True
    except:
        print("Wrong Format, please input correctly\n")
        return False
neutral_analysis("I love cake and whores")

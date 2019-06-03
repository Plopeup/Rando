import re
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

#clean_phrase cleans the phrase from symbols and extra spaces
def clean_phrase(phrase):
    return(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+,)", " ", phrase).split()))

#get_phrase_sentiment will tell if the phrase is a positive,neutral or negative phrase
def get_phrase_sentiment(phrase):
    analysis = TextBlob(clean_phrase(phrase))
    if analysis.sentiment.polarity > 0:
        return('positive')
    if analysis.sentiment.polarity == 0:
        return('neutral')
    else:
        return('negative')

#stop_word_removal removes stop_words from the phrase so that way we can get a list of non-filler words
def stop_word_removal(phrase):
    new_phrase = clean_phrase(phrase)
    new_phrase_list = new_phrase.split(' ')
    stop_words = stopwords.words('english')
    return ([word for word in new_phrase_list if word not in stop_words])

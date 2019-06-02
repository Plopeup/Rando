import re
from textblob import TextBlob

def clean_phrase(phrase):
    return(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", phrase).split()))
def get_phrase_sentiment(phrase):
    analysis = TextBlob(clean_phrase(phrase))
    if analysis.sentiment.polarity > 0:
        return('positive')
    if analysis.sentiment.polarity == 0:
        return('neutral')
    else:
        return('negative')

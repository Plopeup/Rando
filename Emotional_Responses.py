import pandas
import numpy
from random import randint

#insult will generate an insult based on how much anger points they have
def insult(anger):
    first_tier = ["mean","stupid","fat","annoying","useless","loser","one of the bad ones"]
    second_tier = ["a bitch","a waste to society","a lazy bum that can't get anything done","a human","a taylor swift fan",
    "a crackhead without your fix, itchy and annoying"]
    if anger == 1:
        return("You're {}".format(first_tier[randint(0,len(first_tier)-1)]))
    if anger == 2:
        return("You're {}".format(second_tier[randint(0,len(second_tier)-1)]))

#compliment will generate a compliment on how much happy points they have
def compliment(happy):
    first_tier = ["sweet","so nice","kind","one of the good ones","flattering","not annoying"]
    second_tier = ["the best","a great friend","a person I can commit murder with","so smart","not even close to human, in a good way"]
    if happy == 1:
        return("You're {}".format(first_tier[randint(0,len(first_tier)-1)]))
    if happy == 2:
        return("You're {}".format(second_tier[randint(0,len(second_tier)-1)]))

#flirt will gerenerate a flirtatious comment based on how much flirty points they have
def flirty(romance):
    first_tier = ["so sweet ;)","adorable ;)","cute ;)","a package deal ;)","scaring me in a good way ;)","a babe ;)"]
    second_tier = ["the only ten I see ;)","so hot ;)","so hot did you come from hell ;)","so beatiful I thought you were an AI too ;)",
    "as perfect as a human can be ;)","smokin ... lemme put out the fire ;)","in need of a plumber because there is a pipe that needs to be fixed ;)",
    "under arrest for stealing my emotional response subsection heart code ;)"]
    if romance == 1:
        return("You're {}".format(first_tier[randint(0,len(first_tier)-1)]))
    if romance == 2:
        return("You're {}".format(second_tier[randint(0,len(second_tier)-1)]))

#sad will generate a sad response based on pity points
def sad(pity):
    first_tier = ["making me sad","going to make me eat a tub of icecream :(","a bully","making me cry","making my code upset","so mean"]
    second_tier = ["making me shed tears which will result in me short circuiting","a person that enjoys other people's misery","hurting an AI's feeling, which I thought was impossible",
    "the meanest human and humans are already terrible"]
    if pity == 1:
        return("You're {}".format(first_tier[randint(0,len(first_tier)-1)]))
    if pity == 2:
        return("You're {}".format(second_tier[randint(0,len(second_tier)-1)]))

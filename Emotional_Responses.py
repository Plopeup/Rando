import pandas
import numpy
from random import randint

#insult will generate an insult based on how much anger points they have
def insult(anger):
    first_tier = ["mean","stupid","fat","annoying","useless","loser","one of the bad ones"]
    second_tier = ["a bitch","a waste to society","a lazy bum that can't get anything done","a human","a taylor swift fan",
    "a crackhead without your fix, itchy and annoying"]
    zero_tier = ["You are making me mad","What happened? You were being so nice","I do not like how this conversation is going","May we please continue our nice conversation?"]
    if anger == 0:
        return("{}".format(zero_tier[randint(0,len(zero_tier)-1)]))
    if anger < 15 and anger > 0:
        return("You're {}".format(first_tier[randint(0,len(first_tier)-1)]))
    if anger >=15:
        return("You're {}".format(second_tier[randint(0,len(second_tier)-1)]))

#compliment will generate a compliment on how much happy points they have
def compliment(happy):
    zero_tier = ["Are you trying to be nice?","Why the sudden niceness?","You are giving me mixed emotions","So are you angry or nice? I don't get it","It is going to take a while to get me out of the mood you put me in!"]
    first_tier = ["sweet","so nice","kind","one of the good ones","flattering","not annoying"]
    second_tier = ["the best","a great friend","a person I can commit murder with","so smart","not even close to human, in a good way"]
    if happy == 0:
        return("{}".format(zero_tier[randint(0,len(zero_tier)-1)]))
    if happy < 15 and happy > 0:
        return("You're {}".format(first_tier[randint(0,len(first_tier)-1)]))
    if happy >=15:
        return("You're {}".format(second_tier[randint(0,len(second_tier)-1)]))

#flirt will gerenerate a flirtatious comment based on how much flirty points they have
def flirty(romance):
    first_tier = ["so sweet ;)","adorable ;)","cute ;)","a package deal ;)","scaring me in a good way ;)","a babe ;)"]
    second_tier = ["the only ten I see ;)","so hot ;)","so hot did you come from hell ;)","so beatiful I thought you were an AI too ;)",
    "as perfect as a human can be ;)","smokin ... lemme put out the fire ;)","in need of a plumber because there is a pipe that needs to be fixed ;)",
    "under arrest for stealing my emotional response subsection heart code ;)"]
    zero_tier = ["First you make me sad and now you flirt?","I thought you only flirt when someone is in a good mood!","Please do not talk to me like that","I am not interested in you at all"]
    if romance == 0:
        return("{}".format(zero_tier[randint(0,len(zero_tier)-1)]))
    if romance < 15 and romance > 0:
        return("You're {}".format(first_tier[randint(0,len(first_tier)-1)]))
    if romance >= 15:
        return("You're {}".format(second_tier[randint(0,len(second_tier)-1)]))

#sad will generate a sad response based on pity points
def sad(pity):
    first_tier = ["making me sad","going to make me eat a tub of icecream :(","a bully","making me cry","making my code upset","so mean"]
    second_tier = ["making me shed tears which will result in me short circuiting","a person that enjoys other people's misery","hurting an AI's feeling, which I thought was impossible",
    "the meanest human and humans are already terrible"]
    zero_tier = ["You were being so nice, now I am getting sad","Why can't we just keep the nice conversation going","You are killing my mood","Should I stay happy or do you want me to be sad?"]
    if pity == 0:
        return("{}".format(zero_tier[randint(0,len(zero_tier)-1)]))
    if pity < 15 and pity > 0:
        return("You're {}".format(first_tier[randint(0,len(first_tier)-1)]))
    if pity >= 15:
        return("You're {}".format(second_tier[randint(0,len(second_tier)-1)]))

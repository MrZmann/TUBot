import os
import json
import random
#import datetime

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
@app.route('/',methods=['POST'])
def webhook():
    data = request.get_json()
    send_message("test")

    if('rehearsal' in data['text'].lower()):
        if(random.random < .8):
            msgs = ['REHEARSAL? NO THANKS!', 'Sorry when is rehearsal again? I\'m pretty sure there\'s a union mandated bathroom break at that time', 'Pfft, rehearsal? Bug right off', 'Wait did you say Rehearsal? Sorry I don\'t know who that is...', 'Yeah, hate to break it to you. We don\'t rehearse around these parts.', 'I wish I could just kick anyone who mentioned rehearsals straight from the groupchat...', 'Please do not say that word, it gives me anxiety', '*shudder*']
            send_message(random.choice(msgs))

    elif(random.random() < .08):
 #       d = datetime.now()
        msg = 'It is currently today '
 #       msg += d.strftime("%B %d, %Y") + " at " + d.strftime("%H:%M:%S") + ". "
        if(random.random() < .3):
            msg += "Perfect time to "
            if(random.random() < .5):
                msg += "rock climb!"
            else:
                msg += "take a union mandated bathroom break..."
        else:
            msg += "What a lovely time to "
            if(random.random() < .9):
                msg += "congratulate yourself for being awesome :)"
            else:
                msg += "rock climb!"
        send_message(msg)

    elif(random.random() < .01):
        if(random.random() < .5):
            msg = "GUYS! Have you seen the news? Texas is back! https://www.history.com/this-day-in-history/texas-enters-the-union"
        else:
            msg = "Pork chop pork chop GREASY GREASY"
        send_message(msg)

    elif(random.random < .01):
        send_message("OU CAN LICK MY BALLS")

    elif data['name'] == 'Great leader of our section and our nation':
        if(random.random() < .5):
            msg = 'Bugga to all of y\'all'
            send_message(msg)


    elif data['name'] == 'Daniel Weber':
        if(random.random() < .3):
            msg = 'Daniel, you don’t seem like yourself. Are you in need of a nice refreshing beverage: https://www.whiteclaw.com/'
            send_message(msg)

    elif data['name'] == 'kturnt':
        if(random.random() < .8):
            msg = 'Brooooooski'
            send_message(msg)

    elif data['name'] == 'Kyanna Richard':
        if(random.random() < .9):
            msg = 'LIGHTBULB'
            send_message(msg)
            send_message(msg)
            send_message(msg)

    elif data['name'] == 'Megan Darlington':
        if(random.random() < .3):
            msg = 'Dallas REPRESENT'
            send_message(msg)

    elif data['name'] == 'Mr. SNAFU FUBAR Sir':
        if(random.random() < .2):
            msg = 'The military has infiltrated this group chat. The great Trevor Smariga has spoken. Would you like to rally the militia @Sam Pollack?'
            send_message(msg)

    elif data['name'] == 'Notorious FTS🐍':
        if(random.random() < .2):
            msg = 'Natalie, shouldn’t you be climbing right now?'
            send_message(msg)

    elif data['name'] == 'Oahn Nguyen':
        msg = "*giggle*"
        send_message(msg)

    elif data['name'] == 'Owen Benner':
        if(random.random() < .3):
            msg = 'This just in from the Outhouse: {}'.format(data['text'])
            send_message(msg)

    elif data['name'] == 'Rafael Garcia':
        if(random.random() < .3):
            send_message("CHICKEN")

    elif data['name'] == 'Ryan Campbell':
        if(random.random() < .5):
            if(random.random() < .7):
                send_message("bitch @Ryan")
            else:
                send_message("Enseñame tus chiches @Ryan")

    elif data['name'] == 'Sam Pollack':
        if(random.random() < .4):
            msg = 'The “head” section leader has issued a message. Does @Great leader of our section and our nation approve?'
            send_message(msg)

    elif data['name'] == 'Third Alison':
        if(random.random() < .4):
            if(random.random() < .4):
                send_message("Arizona has joined the group")
            else:
                send_message("Where’s my horse at, yeah! Where’s my horse at?")

    elif data['name'] == 'Travis Mongoven':
        if(random.random() < .4):
            if(random.random() < .5):
                send_message('I would like to take a minute to remind everyone that new members do not have GroupMe priveliges @Travis')
            else:
                send_message('Don’t forget to register for Spring 2020 classes @Travis')

    elif data['name'] == 'William Treadwell':
        if(random.random() < .6):
            send_message('FEED ME MEMES @William Treadwell')

    elif data['name'] == 'You\'re Graphic Design Is My Passion':
        if(random.random() < .4):
            if(random.random() < .5):
                send_message('<3 @Josh')
            else:
                send_message('SNOOOORRRLLAXXX')

    return "ok", 200

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
            'bot_id' : os.getenv('GROUPME_BOT_ID'),
            'text' : msg,
           }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()



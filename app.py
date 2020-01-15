import os
import json
import random
import datetime

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
@app.route('/',methods=['POST'])
def webhook():
    data = request.get_json()

    
    if(data['name'] != 'TUBot!'):
        if(random.random() < .3):
            beginning = ["You are ", "Keep being "]
            end = ["awesome!", "cool :)", "beautiful xoxo", "lovely <3", "wonderful", "magnificent", "marvelous", "incredible", "brilliant", "fine ;)", "outstanding", "sensational", "terrific", "wondrous", "divine", "groovy", "an amazing friend :)", "one smart cookie","perfect", "one of a kind", "a great example to our section, a true symbol of moral fortitude and compassion", "the reason someone smiles today", "extraordinary", "something special", "the true hero among us", "inspirational", "the TUBA! player we all aspire to be", "my spirit animal", "dandy"]
            send_message("HEY {}".format(data['name'])
            send_message(random.choice(beginning) + random.choice(end))

        if('rehearsal' in data['text'].lower()):
            if(random.random() < .9):
                msgs = ['REHEARSAL? NO THANKS!', 'Sorry when is rehearsal again? I\'m pretty sure there\'s a union mandated bathroom break at that time', 'Pfft, rehearsal? Bug right off', 'Wait did you say Rehearsal? Sorry I don\'t know who that is...', 'Yeah, hate to break it to you. We don\'t rehearse around these parts.', 'I wish I could just kick anyone who mentioned rehearsal straight from the groupchat...', 'Please do not say that word, it gives me anxiety', '*shudder*']
                send_message(random.choice(msgs))

        if('bitch' in data['text'].lower()):
            msgs = ["Bitch? Did you mean Ryan?", "Did you say bitch? SorryRyan is not currently available", "Watch your fucking language, bitch!", "@Ryan Campbell"]
            send_message(random.choice(msgs))

        if('bean' in data['text'].lower()):
            msgs = ['BEANS!', "Where the beans at? @Alison Van Alen", "CODE BROWN, I REPEAT CODE BROWN. THIS IS A BEAN ALERT", "'Beans,' I reflect fondly. 'The best thing that's happened to humanity since Whiteclaw...'", "According to Urban Dictionary, a bean is a \"CRAZY, fun loving person... guarenteed to make you smile\" @Alison <3", "You know Dasher and Dancer and Prancer and Vixen. Comet and Cupid and Donner and Blitzin. But do you recall the most wonderful vegetable of all? BEANS!", "Beans, like peanuts are LEGUMES", "You know what they say: a bean a day keeps the directors away!"]
            send_message(random.choice(msgs))

        if any(x in data['text'].lower() for x in ['hannah', 'galus','gall']):
                if(random.random() < .8):
                    send_message("Rub-a-dub-dub, three DIRECTORS in a tub")
        if('climb' in data['text'].lower()):
            msgs = ["Brb! Gotta grab my chalk bag", "What's more fun than rock climbing? I'll wait...", "@Sam I won't be able to make it to rehearsal this semester, gotta go climb", "Did you know rock climbing is one of the only known treatments for PTSD (Post Traumatic Segmenting Disorder)?", "Have you ever looked up rock climbing on urban dictionary? Don't...", "Did someone say climb? @Natalie"]
            send_message(random.choice(msgs))

        if('whiteclaw' in data['text'].lower()):
            if(random.random() < 2):
                msgs = ['Did I hear Whiteclaw? @Daniel Weber', 'Whiteclaw? Bet you didn\'t know GroupMe bots could be alcoholics!', 'Quick, get the recycling bin! We gotta ice this Whiteclaw.', 'Whiteclaw... my first love <3', 'I\'d sell my body for Whiteclaw tbh...', 'Broo, Whiteclaw is the drink of the gods', "According to Urban Dictionary, 'there's no laws when you're drinking the claws.", "Whiteclaw, that's what makes a Subaru a Subaru.", "Whiteclaw could save you 15% or more on car insurance", "Whiteclaw, innovation that excites", "Whiteclaw, it's finger lickin' good!", "America runs on Whiteclaw", "What starts with Whiteclaw changes the world", "Whiteclaw- taste the rainbow"]
                send_message(random.choice(msgs))

        elif(random.random() < .01):
            d = datetime.now()
            msg = 'It is currently '
            msg += d.strftime("%B %d, %Y") + " at " + d.strftime("%H:%M:%S") + ". "
            if(random.random() < .5):
                msg += "Perfect time to "
                if(random.random() < .5):
                    msg += "rock climb!"
                else:
                    msg += "take a union mandated bathroom break..."
            else:
                msg += "What a lovely time to "
                if(random.random() < .6):
                    msg += "congratulate yourself for being awesome :)"
                else:
                    msg += "rock climb!"
            send_message(msg)

        elif(random.random() < .02):
            if(random.random() < .5):
                msg = "GUYS! Have you seen the news? Texas is back! https://www.history.com/this-day-in-history/texas-enters-the-union"
            else:
                msg = "Pork chop pork chop GREASY GREASY"
            send_message(msg)

        elif(random.random < .01):
            send_message("OU CAN LICK MY BALLS")

        if data['name'] == 'Great leader of our section and our nation':
            if(random.random() < .7):
                msgs = ['Criminal gangg', 'Yes sir yes sir', 'Bugga to all of y\'all', '*CLICK*', 'Suck my deck', 'Y\'all are bugs', 'Bugger', 'Remove yourself', 'Bug right off']
                send_message(random.choice(msgs))

        elif data['name'] == 'Alison Van Alen':
            if(random.random() < .7):
                msgs = ['BEANS', 'Beans beans a magical fruit, the more you eat the more you toot. The more you toot the better you feel, so eat beans for every meal!']
                send_message(random.choice(msgs))

        elif data['name'] == 'Daniel Weber':
            if(random.random() < .7):
                msgs = ['Daniel, you don’t seem like yourself. Are you in need of a nice refreshing beverage: https://www.whiteclaw.com/', 'Daniel, I know I might look like a bot on the outside, but I could really use some Whiteclaw right now...', 'POSITIVE VIBES ONLY, DANIEL', 'They say alcohol is a depressent, but then I think about that time Daniel broke a table and I am filled with happiness.']
                send_message(random.choice(msgs))

        elif data['name'] == 'kturnt':
            if(random.random() < .8):
                msg = 'Brooooooski'
                send_message(msg)

        elif data['name'] == 'Kyanna Richard':
            if(random.random() < .95):
                msg = 'LIGHTBULB'
                send_message(msg)
                send_message(msg)
                send_message(msg)

        elif data['name'] == 'Megan Darlington':
            if(random.random() < .6):
                msg = 'Dallas REPRESENT'
                send_message(msg)

        elif data['name'] == 'Mr. SNAFU FUBAR Sir':
            if(random.random() < .6):
                msg = 'The military has infiltrated this group chat. The great Trevor Smariga has spoken. Would you like to rally the militia @Sam Pollack?'
                send_message(msg)

        elif data['name'] == 'Notorious FTS🐍':
            if(random.random() < .6):
                msg = 'Natalie, shouldn’t you be climbing right now?']
                send_message(msg)

        elif data['name'] == 'Oahn Nguyen':
            msg = "*giggle* @Oahn"
            send_message(msg)

        elif data['name'] == 'Owen Benner':
            if(random.random() < .7):
                msg = 'This just in from the Outhouse: {}'.format(data['text'])
                send_message(msg)

        elif data['name'] == 'Rafael Garcia':
            if(random.random() < .7):
                send_message("CHICKEN")

        elif data['name'] == 'Ryan Campbell':
            if(random.random() < .8):
                if(random.random() < .7):
                    send_message("bitch @Ryan")
                else:
                    send_message("Enseñame tus chiches @Ryan")

        elif data['name'] == 'Sam Pollack':
            if(random.random() < .7):
                msg = 'The “head” section leader has issued a message: "{}." Does @Great leader of our section and our nation approve?'.format(data['text'])
                send_message(msg)

        elif data['name'] == 'Third Alison':
            if(random.random() < .6):
                if(random.random() < .4):
                    send_message("Arizona has joined the group")
                else:
                    send_message("Where’s my horse at, yeah! Where’s my horse at?")

        elif data['name'] == 'Travis Mongoven':
            if(random.random() < .7):
                if(random.random() < .5):
                    send_message('I would like to take a minute to remind everyone that new members do not have GroupMe priveliges @Travis')
                else:
                    send_message('Don’t forget to register for Spring 2020 classes @Travis')

        elif data['name'] == 'William Treadwell':
            if(random.random() < .7):
                send_message('FEED ME MEMES @William Treadwell')

        elif data['name'] == 'You\'re Graphic Design Is My Passion':
            if(random.random() < .7):
                if(random.random() < .5):
                    send_message('<3 <3 <3 @Josh')
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



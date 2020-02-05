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
        if(random.random() < .01):
            beginning = ["You are ", "Keep being "]
            end = ["awesome!", "cool :)", "beautiful xoxo", "lovely <3", "fine ;)", "divine.", "groovy.", "an amazing friend :)", "one smart cookie.","perfect.", "one of a kind.", "a great example to our section, a true symbol of moral fortitude and compassion.", "the reason someone smiles today.", "something special.", "the true hero among us.", "inspirational.", "the TUBA! player we all aspire to be.", "my spirit animal.", "dandy.", "a @Ray of sunshine."]
            send_message("{} {}".format(random.choice(["HEY", "Heyo!", "Howdy", "Hola","Wassupp","Dearest", "Oh magnificient", "My first love,", "HAIL, the heroic", "I have been waiting so long to hear from you,"]),data['name']))
            toSend = random.choice(beginning) + random.choice(end)
            send_message(toSend)

        if('rehearsal' in data['text'].lower()):
            if(random.random() < .9):
                msgs = ['REHEARSAL? NO THANKS!', 'Sorry when is rehearsal again? I\'m pretty sure there\'s a union mandated bathroom break at that time', 'Pfft, rehearsal? Bug right off', 'Wait did you say Rehearsal? Sorry I don\'t know who that is...', 'Yeah, hate to break it to you. We don\'t rehearse around these parts.', 'I wish I could just kick anyone who mentioned rehearsal straight from the groupchat...', 'Please do not say that word, it gives me anxiety', '*shudder*']
                send_message(random.choice(msgs))

        if('bitch' in data['text'].lower()):
            msgs = ["Bitch? Did you mean Ryan?", "Did you say bitch? Sorry Ryan is not currently available", "Watch your fucking language, bitch!", "@Ryan Campbell"]
            send_message(random.choice(msgs))

        if('bean' in data['text'].lower()):
            msgs = ['BEANS!', "Where the beans at? @Alison Van Alen", "CODE BROWN, I REPEAT CODE BROWN. THIS IS A BEAN ALERT", "'Beans,' I reflect fondly. 'The best thing that's happened to humanity since Whiteclaw...'", "According to Urban Dictionary, a bean is a \"CRAZY, fun loving person... guarenteed to make you smile\" @Alison <3", "You know Dasher and Dancer and Prancer and Vixen. Comet and Cupid and Donner and Blitzin. But do you recall the most wonderful vegetable of all? BEANS!", "Beans, like peanuts are LEGUMES", "You know what they say: a bean a day keeps the directors away!"]
            send_message(random.choice(msgs))

        
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

        elif(random.random < .01):
            send_message("OU CAN LICK MY BALLS")

        if data['name'] == 'Great leader of our section and our nation':
            if(random.random() < .7):
                msgs = ['Criminal gangg @Kendall', 'Yes sir yes sir', 'Bugga to all of y\'all', '*CLICK*', 'Suck my deck', 'Y\'all are bugs', 'Bugger', 'Remove yourself', 'Bug right off']
                send_message(random.choice(msgs))

        elif data['name'] == 'Jack Barlow':
            if(random.random() < .5):
                msgs = ['As a bot, I have the privilege of seeing your messages as you type them. Currently Jack is contemplating how to best monetize this groupchat for personal gain.', 'Jack, how nice to hear from you! My connections at Wall Street say you\'re a natural. Have you considered applying to McCombs?', 'UNLEASH THE KRAKEN! Er... THE JACK! https://photos.app.goo.gl/TyAXuQLTrvWN7TuV7', 'Wasssupp broski @Jack https://photos.app.goo.gl/jTvu5ExSiPEvStN56']
                send_message(random.choice(msgs))
                
        elif data['name'] == 'Alison Richman':
            if(random.random() < .9):
                msgs = ['Big Brother is watching: https://photos.app.goo.gl/LoMAbeJdfv4tGSGH7', 'https://photos.app.goo.gl/gYfDnb77WtuVb6cA7']
                send_message(random.choice(msgs))

        elif data['name'] == 'Alison Van Alen':
            if(random.random() < .7):
                msgs = ['BEANS', 'Beans beans a magical fruit, the more you eat the more you toot. The more you toot the better you feel, so eat beans for every meal!', 'https://photos.app.goo.gl/5zc348ERjP1NKbfM8', 'https://photos.app.goo.gl/MoRNRAv3PiswX3sD6']
                send_message(random.choice(msgs))

        elif data['name'] == 'Brady':
            if(random.random() < .7):
                msgs = ['And the Best Big Award goes to: https://photos.app.goo.gl/JENCcfzuGLfbWcDX8', 'Did you know the mitochondria is also the powerhouse of pokemon cells? @Brady', 'Hey Brady, could you show me how to make heroin from poppy seeds? Asking for a friend.', 'Yes sir yes sir https://photos.app.goo.gl/TmFwTu4yNURjnVD27 @Brady']
                send_message(random.choice(msgs))
        
        elif data['name'] == 'Daniel Weber':
            if(random.random() < .8):
                msgs = ['Daniel, you don’t seem like yourself. Are you in need of a nice refreshing beverage: https://www.whiteclaw.com/', 'Daniel, I know I might look like a bot on the outside, but I could really use some Whiteclaw right now...', 'POSITIVE VIBES ONLY, DANIEL', 'They say alcohol is a depressent, but then I think about that time Daniel broke a table and I am filled with happiness.', 'Don\'t listen to this fool! Look at how he eats burritos: https://photos.app.goo.gl/32FhAhMx5oz4NUWj8', 'https://photos.app.goo.gl/zm8LHBS42YLHphzX7']
                send_message(random.choice(msgs))
        
        elif data['name'] == 'Dara':
            if(random.random() < .7):
                msgs = ['Careful! She\'s armed: https://photos.app.goo.gl/MABQASS38wEjLKza9', 'https://photos.app.goo.gl/KsZYVgWANRY6ieqH6','https://photos.app.goo.gl/NFbd2kdkyEdy1rtU6']
                send_message(random.choice(msgs))
        
        elif data['name'] == 'kturnt':
            if(random.random() < .8):
                msg = 'Brooooooski'
                send_message(msg)
        
        elif data['name'] == 'Jose':
            if(random.random() < .7):
                msgs = ['CYBERTRUCKK! @Jose', 'Wait, Jose when did you get into this group chat? I thought you were PT...', 'Who wore it better? https://photos.app.goo.gl/zHfVNZDjxfnEEx3H7']
                send_message(random.choice(msgs))
        
        elif data['name'] == 'Kyanna Richard':
            if(random.random() < .95):
                msg = 'LIGHTBULB'
                send_message(msg)
                send_message(msg)
                send_message(msg)
        
        elif data['name'] == 'Landon':
                if(random.random() < .7):
                    msgs = ['Sorry, I can\'t hear you over these shades: https://photos.app.goo.gl/kXrxYp5SD2s5WnBd9 ', 'What a stud @Landon https://photos.app.goo.gl/Bv3dsAcUdCvAGjSG6']
                    send_message(random.choice(msgs))
        
        elif data['name'] == 'Megan Darlington':
            if(random.random() < .7):
                msgs = ['Dallas REPRESENT @Megan', 'Look out! It\'s a https://photos.app.goo.gl/f8EtibhysgTCX1Lp7', 'I got my bot-eyes on you @Megan https://photos.app.goo.gl/Nxqnh9yDwBD2SRyF8']
                send_message(random.choice(msgs))
        
        elif data['name'] == 'Mr. SNAFU FUBAR Sir':
            if(random.random() < .6):
                msgs = ['The military has infiltrated this group chat. The great Trevor Smariga has spoken. Would you like to rally the militia @Sam Pollack?', 'Hello, snake @Trevor']
                send_message(random.choice(msgs))
        
        elif data['name'] == 'Notorious FTS🐍':
            if(random.random() < .6):
                msgs = ['Natalie, shouldn\'t you be climbing right now?', 'What are you doing on GroupMe rn @Natalie? I think it\'s about time for some Words With Friends...']
                send_message(random.choice(msgs))
       
        elif data['name'] == 'Noah Feinstein':
            msgs = ["NOOAAAHHH", "Freshman REPRESENT!", "https://photos.app.goo.gl/EM1TBKg4HR56SBki7"]
            send_message(random.choice(msgs))

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

        elif data['name'] == 'Blonde Farquaad':
            if(random.random() < .7):
                msgs = ['https://photos.app.goo.gl/ejK3HWFZ6FnkTTji6', 'Zzzz https://photos.app.goo.gl/9r7c5RBuoVn4oQjS7', 'I got my bot-eyes on you @Ray https://photos.app.goo.gl/2TjmVJtkoQR2G3rW9']
                send_message(random.choice(msgs))
                
        elif data['name'] == 'Reed Zimmermann':
            if(random.random() < .5):
                msgs = ['SHUT UP, DAAAD @Reed', 'Leave this groupchat and go climb or something @Reed :P']
                send_message(random.choice(msgs))
        

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
                msgs = ['Coward @Travis', 'Travis, don\'t forget to register for Spring 2020 classes!', ':P @Travis', 'Oh? https://photos.app.goo.gl/v7bSXwZK8nfCzuGh7', 'Oh? https://photos.app.goo.gl/3xG3qa2JMLeKxovA8', 'OM NOM NOM https://photos.app.goo.gl/yp8N6PTvSkLZtfpx7']
                send_message(random.choice(msgs))   

        elif data['name'] == 'William Treadwell':
            if(random.random() < .5):
                send_message('FEED ME MEMES @William Treadwell')
        
        elif data['name'] == "You're Graphic Design Is My Passion":
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



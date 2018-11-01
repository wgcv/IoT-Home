## website.py
import os
import json
from pprint import pprint
from flask import Flask
from flask_ask import Ask, statement, question, session
from flask import request
myapikey = 'XXXXX'
app = Flask(__name__)
ask = Ask(app, '/')
what = 'You can repete?'
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/tvdoppio/power', methods=['GET'])
def power():
    api_key = request.args.get('username')
    if(myapikey == api_key):
        os.system('irsend SEND_ONCE TVDOPPIO POWER')
        return 'Ok 200'
    else:
        return 'not ok 200'

@app.route('/tvdoppio/volume/down')
def volumeDown():
    api_key = request.args.get('username')
    if(myapikey == api_key):
        os.system('irsend SEND_ONCE TVDOPPIO VOLUMEDOWN')
        return 'Ok 200'
    else:
        return 'not ok 200'

@app.route('/tvdoppio/volume/up')
def volumeUp():
    api_key = request.args.get('username')
    if(myapikey == api_key):
        os.system('irsend SEND_ONCE TVDOPPIO VOLUMEUP')
        return 'Ok 200'
    else:
        return 'not ok 200'

@app.route('/tvdoppio/mute')
def volumeMute():
    api_key = request.args.get('username')
    if(myapikey == api_key):
        os.system('irsend SEND_ONCE TVDOPPIO MUTE')
        return 'Ok 200'
    else:
        return 'not ok 200'

@app.route('/tvdoppio/sleep')
def tvSleep():
    api_key = request.args.get('username')
    if(myapikey == api_key):
        os.system('irsend SEND_ONCE TVDOPPIO SLEEP')
        return 'Ok 200'
    else:
        return 'not ok 200'

@app.route('/tvdoppio/input')
def tvInput():
    api_key = request.args.get('username')
    if(myapikey == api_key):
        os.system('irsend SEND_ONCE TVDOPPIO VIDEO')
        return 'Ok 200'
    else:
        return 'not ok 200'

@ask.launch
def start_skill():
    print('welcom')
    welcome_message = 'I\'m Dino and I can help you with the weather. How should update the air conditioner?'
    return question(welcome_message)

# Air conditioner Auto
@ask.intent('AirConditionerAutoIntent', convert={'air_value_auto': str})
def air_condtioner_intent_auto(air_value_auto):
    if (air_value_auto is None):
        text = 'None'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA POWER')
        return statement(what)
    if ( air_value_auto == 'off' or air_value_auto == 'turn off' ):
        text = 'Turning off the air conditioner'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TURNOFF')
    elif air_value_auto.lower() == '17':
        text = 'The energy, stop! Okey, the air conditioner is in auto 17'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO17')
    elif ( air_value_auto.lower() == '18' ):
        text = 'The air conditioner is in auto 18'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO18')
    elif ( air_value_auto.lower() == '19' ):
        text = 'That is so could! The air conditioner is in auto 19'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO19')
    elif ( air_value_auto.lower() == '20' ):
        text = 'The air conditioner is in auto 20'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO20')
    elif ( air_value_auto.lower() == '21' ):
        text = 'The air conditioner is in auto 21'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO21')
    elif ( air_value_auto.lower() == '22' ):
        text = 'The air conditioner is in auto 22'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO22')
    elif ( air_value_auto.lower() == '23' ):
        text = 'The air conditioner is in auto 23'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO23')
    elif ( air_value_auto.lower() == '24' ):
        text = 'The air conditioner is in auto 24'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO24')
    elif ( air_value_auto.lower() == '25' ):
        text = 'The air conditioner is in auto 25'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO25')
    elif ( air_value_auto.lower() == '26' ):
        text = 'The air conditioner is in auto 26'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO26')
    elif ( air_value_auto.lower() == '27' ):
        text = 'The air conditioner is in auto 27'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO27')
    elif ( air_value_auto.lower() == '28' ):
        text = 'The air conditioner is in auto 28'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO28')
    elif ( air_value_auto.lower() == '29' ):
        text = 'The air conditioner is in auto 29'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO29')
    elif ( air_value_auto.lower() == '30' ):
        text = 'The air conditioner is in auto 30'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA AUTO30')
    elif ( air_value_auto.lower() == 'turbo' ):
        text = 'The air conditioner is your only hope. Now is in turbo'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TURBO')
    elif ( air_value_auto.lower() == 'sleep in 30' ):
        text = 'Is going to turn off in 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER05')
    elif ( air_value_auto.lower() == 'sleep in 1' ):
        text = 'Is going to turn off in 1 hour'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER10')

    elif ( air_value_auto.lower() == 'sleep in 1 30' ):
        text = 'Is going to turn off in 1 hour 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER15')
    elif ( air_value_auto.lower() == 'sleep in 2' ):
        text = 'Good nigth. The air is going to turn off in 2 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER20')

    elif ( air_value_auto.lower() == 'sleep in 2 30' ):
        text = 'Is going to turn off in 2 hours 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER25')
    elif ( air_value_auto.lower() == 'sleep in 3' ):
        text = 'The Force will be with you. Is going to turn off in 3 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER30')
    elif ( air_value_auto.lower() == 'sleep in 3 30' ):
        text = 'Is going to turn off in 3 hours 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER35')
    elif ( air_value_auto.lower() == 'sleep in 4' ):
        text = 'Is going to turn off in 4 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER40')
    elif ( air_value_auto.lower() == 'sleep in 5 30' ):
        text = 'Is going to turn off in 5 hours 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER45')
    elif ( air_value_auto.lower() == 'sleep in 5' ):
        text = 'Is going to turn off in 5 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER50')
    elif ( air_value_auto.lower() == 'sleep in 6' ):
        text = 'Is going to turn off in 6 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER60')
    elif ( air_value_auto.lower() == 'sleep in 7' ):
        text = 'Is going to turn off in 7 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER70')
    elif ( air_value_auto.lower() == 'sleep in 8' ):
        text = 'Is going to turn off in 8 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER80')
    else:
        print(air_value_auto)
        return question(what)
    return statement(text)


# Air conditioner Dry
@ask.intent('AirConditionerDryIntent', convert={'air_value_dry': str})
def air_condtioner_intent_dry(air_value_dry):
    if (air_value_dry is None):
        text = 'None'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA POWER')
        return statement(what)
    if ( air_value_dry == 'off' or air_value_dry == 'turn off' ):
        text = 'Turning off the air conditioner'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TURNOFF')
    elif ( air_value_dry.lower() == '17' ):
        text = 'The air conditioner is in dry 17'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR17')
    elif ( air_value_dry.lower() == '18' ):
        text = 'The air conditioner is in dry 18'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR18')
    elif ( air_value_dry.lower() == '19' ):
        text = 'The air conditioner is in dry 19'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR19')
    elif ( air_value_dry.lower() == '29' ):
        text = 'The air conditioner is in dry 29'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR20')
    elif ( air_value_dry.lower() == '21' ):
        text = 'The air conditioner is in dry 21'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR21')
    elif ( air_value_dry.lower() == '22' ):
        text = 'The air conditioner is in dry 22'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR22')
    elif ( air_value_dry.lower() == '23' ):
        text = 'The air conditioner is in dry 23'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR23')
    elif ( air_value_dry.lower() == '24' ):
        text = 'The air conditioner is in dry 24'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR24')
    elif ( air_value_dry.lower() == '25' ):
        text = 'The air conditioner is in dry 25'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR25')
    elif ( air_value_dry.lower() == '26' ):
        text = 'The air conditioner is in dry 26'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR26')
    elif ( air_value_dry.lower() == '27' ):
        text = 'The air conditioner is in dry 27'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR27')
    elif ( air_value_dry.lower() == '28' ):
        text = 'The air conditioner is in dry 28'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR28')
    elif ( air_value_dry.lower() == '29' ):
        text = 'The air conditioner is in dry 29'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR29')
    elif ( air_value_dry.lower() == '30' ):
        text = 'The air conditioner is in dry 30'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA SECAR30')
    elif ( air_value_dry.lower() == 'turbo' ):
        text = 'The air conditioner is your only hope. Now is in turbo'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TURBO')
    elif ( air_value_dry.lower() == 'sleep in 30' ):
        text = 'Is going to turn off in 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER05')
    elif ( air_value_dry.lower() == 'sleep in 1' ):
        text = 'Is going to turn off in 1 hour'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER10')
    elif ( air_value_dry.lower() == 'sleep in 1 30' ):
        text = 'Is going to turn off in 1 hour 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER15')
    elif ( air_value_dry.lower() == 'sleep in 2'):
        text = 'Good nigth. The air is going to turn off in 2 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER20')
    elif ( air_value_dry.lower() == 'sleep in 2 30' ):
        text = 'Is going to turn off in 2 hours 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER25')
    elif ( air_value_dry.lower() == 'sleep in 3' ):
        text = 'The Force will be with you. Is going to turn off in 3 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER30')
    elif ( air_value_dry.lower() == 'sleep in 3 30' ):
        text = 'Is going to turn off in 3 hours 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER35')
    elif ( air_value_dry.lower() == 'sleep in 4' ):
        text = 'Is going to turn off in 4 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER40')
    elif ( air_value_dry.lower() == 'sleep in 5 30' ):
        text = 'Is going to turn off in 5 hours 30 minuts'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER45')
    elif ( air_value_dry.lower() == 'sleep in 5' ):
        text = 'Is going to turn off in 5 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER50')
    elif ( air_value_dry.lower() == 'sleep in 6' ):
        text = 'Is going to turn off in 6 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER60')
    elif ( air_value_dry.lower() == 'sleep in 7' ):
        text = 'Is going to turn off in 7 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER70')
    elif ( air_value_dry.lower() == 'sleep in 8' ):
        text = 'Is going to turn off in 8 hours'
        print(text)
        os.system('irsend SEND_ONCE ACINDURAMA TIMER80')
    else:
        print(air_value_dry)
        return question(what)
    return statement(text)

# Air conditioner Fan
@ask.intent('AirConditionerFanIntent', convert={'fan_value': str})
def air_condtioner_intent_fan(fan_value):
    # Tell LIRC to send IR LED blink pattern to turn TV on/off
    os.system('irsend SEND_ONCE ACINDURAMA FANAUTO')
    text = 'Turning the air {}'.format(fan_value)
    return statement(text)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4040)

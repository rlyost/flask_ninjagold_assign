from flask import Flask, render_template, request, redirect, session
import random
from time import gmtime, strftime

app = Flask(__name__)
app.secret_key = 'freelunch'

@app.route('/')
def home():
    if not session.get('your_gold'):
        session['your_gold'] = 0
        session['activities'] = []
        session['temp'] = 0
        session['newline'] = -1
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def check():
    session['newline'] += 1
    if request.form['building'] == 'farm':
        session['temp'] = random.randrange(10, 21)
        session['your_gold'] += session['temp'] 
        temp2 = "Earned ", str(session['temp']), " golds from the farm!    ", strftime("%Y-%m-%d %H:%M:%S", gmtime())
        temp3 = "".join(temp2)
        session['activities'].append(temp3)
    elif request.form['building'] == 'cave':
        session['temp'] = random.randrange(5, 11)
        session['your_gold'] += session['temp']
        temp2 = "Earned ",str(session['temp'])," golds from the cave!   ", strftime("%Y-%m-%d %H:%M:%S", gmtime())
        temp3 = "".join(temp2)
        session['activities'].append(temp3)
    elif request.form['building'] == 'house':
        session['temp'] = random.randrange(2, 6)
        session['your_gold'] += session['temp']
        temp2 = "Earned ",str(session['temp'])," golds from the house!   ", strftime("%Y-%m-%d %H:%M:%S", gmtime())
        temp3 = "".join(temp2)
        session['activities'].append(temp3)
    elif request.form['building'] == 'casino':
        session['temp'] = random.randrange(0, 101)-50
        session['your_gold'] += session['temp']
        if session['temp'] > 0:
            temp2 = "Earned ",str(session['temp'])," golds from the casino!   ", strftime("%Y-%m-%d %H:%M:%S", gmtime())
            temp3 = "".join(temp2)
            session['activities'].append(temp3)
        else:
            temp2 = "Entered a casino and lost ",str(-session['temp']),".....Ouch! ", strftime("%Y-%m-%d %H:%M:%S", gmtime())
            temp3 = "".join(temp2)
            session['activities'].append(temp3)    
    return redirect('/')

@app.route('/reset')
def reset():
    # reset the gold and activities redirect to the home page
    session['your_gold'] = 0
    session['activities'] = ""
    session['newline'] = -1
    return redirect('/')

app.run(debug=True)
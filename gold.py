from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'freelunch'

@app.route('/')
def home():
    if not session.get('your_gold'):
        session['your_gold'] = 0
        session['activities'] = ""
        session['temp'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def check():
    if request.form['value'] == 'farm':
        session['temp'] = random.randrange(10, 21)
        session['your_gold'] += session['temp']
        session['activities'] += "Earned ",session['temp']," golds from the farm! ", time
    elif request.form['value'] == 'cave':
        session['temp'] = random.randrange(5, 11)
        session['your_gold'] += session['temp']
        session['activities'] += "Earned ",session['temp']," golds from the cave! ", time
    elif request.form['value'] == 'house':
        session['temp'] = random.randrange(2, 6)
        session['your_gold'] += session['temp']
        session['activities'] += "Earned ",session['temp']," golds from the house! ", time
    elif request.form['value'] == 'casino':
        session['temp'] = random.randrange(0, 101)-50
        session['your_gold'] += session['temp']
        if session['temp'] > 0:
            session['activities'] += "Earned ",session['temp']," golds from the house! ", time
        else:
            session['activities'] += "Entered a casino and lost",session['temp'],".....Ouch! ", time
    return redirect('/')

@app.route('/reset')
def reset():
    # reset the gold and activities redirect to the home page
    session['your_gold'] = 0
    session['activities'] = ""
    return redirect('/')

app.run(debug=True)
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def home():
    if not session.get('your_gold'):
        session['your_gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def check():
    if request.form['value'] == 'farm':
        session['your_gold'] += random.randrange(10, 21)
    elif request.form['value'] == 'cave':
        session['your_gold'] = random.randrange(5, 11)
    elif request.form['value'] == 'house':
        session['your_gold'] = random.randrange(2, 6)
    elif request.form['value'] == 'casino':
        session['your_gold'] = random.randrange(0, 101)-50 
    return redirect('/')

# @app.route('/reset')
# def reset():
#     # reset the random number and redirect to the home page
#     session['your_gold'] = 0
#     return redirect('/')

app.run(debug=True)
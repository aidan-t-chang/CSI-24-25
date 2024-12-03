from flask import Flask, render_template, request, redirect, url_for
from random import randrange

app = Flask(__name__)

# Store the pet's status
pet = {
    'name': 'Fluffy',
    'happiness': 5,
    'hunger': 5,
    'bored': 2,
    'skill': 0,
    'iq': 15
}

@app.route('/')
def home():
    return render_template('index.html', pet=pet)

@app.route('/feed')
def feed():
    pet['hunger'] = max(0, pet['hunger'] - 1)
    # if you keep feeding the dog without playing it, the dog will eventually get bored
    pet['bored'] = min(10, pet['bored'] + randrange(0,2))
    return redirect(url_for('home'))

@app.route('/play')
def play():
    pet['happiness'] = min(10, pet['happiness'] + 1)
    #playing with the dog will decrease its boredom
    pet['bored'] = max(0, pet['bored'] - 1)
    return redirect(url_for('home'))

#teach the dog how to do a trick, but sometimes it wont listen (hence the 0 in randrange)
#teaching the dog too much will also make the dog become hungry again
@app.route('/teach')
def teach():
    pet['skill'] += randrange(0,2)
    if randrange(0,3) == 2:
        pet['hunger'] = min(10, pet['hunger'] + 1)
    return redirect(url_for('home'))

# why would you play with another dog?
@app.route('/change')
def change():
    pet['happiness'] = 0
    return redirect(url_for('home'))

# taking the dog on a walk will increase its happiness, but will also make it more hungry.
@app.route('/walk')
def walk():
    pet['happiness'] = min(10, pet['happiness'] + 2)
    pet['hunger'] = min(10, pet['hunger'] + randrange(0,2))
    return redirect(url_for('home'))

# teaching the dog calculus will make it smarter, but also less happy and more bored.
@app.route('/calculus')
def calculus():
    pet['happiness'] = max(0, pet['happiness'] - 2)
    pet['bored'] = min(10, pet['bored'] + 2)
    pet['iq'] += randrange(1, 11)
    return redirect(url_for('home'))

# watching tv with the dog will make it more happy and less bored, but in turn will make it slightly decrease its iq.
@app.route('/tv')
def tv():
    pet['iq'] = max(0, pet['iq'] - randrange(1, 4))
    pet['bored'] = max(0, pet['bored'] - 1)
    pet['happiness'] = 7
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

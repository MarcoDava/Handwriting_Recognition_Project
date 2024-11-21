from bidict import bidict 
from flask import Flask, render_template, request,redirect, url_for

from random import choice

ENCODER = bidict({
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
    'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
})


app = Flask(__name__)

@app.route('/')#"Main menu"
def index():
    return render_template("index.html")

@app.route('/app-data', methods=['GET'])
def add_data_get():
    letter=choice(list(ENCODER.keys()))
    return render_template("addData.html",letter=letter)


@app.route('/app-data', methods=['POST'])
def add_data_post():
    
    print(request.form)

    return redirect(url_for('add_data_get'))


@app.route('/practice', methods=['GET'])
def practice_get():
    return render_template("practice.html")


@app.route('/practice', methods=['POST'])
def practice_post():
    return render_template("practice.html")   



if __name__=='__main__':
    app.run(debug=True)
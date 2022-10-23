# package imports
from flask import Flask, render_template, url_for, request
import joblib
from joblib import dump, load

# NLP Packages
from textblob import TextBlob,Word 
import random 
import time

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def question():
	return render_template('question.html')




if __name__ == '__main__':
	app.run(debug=True)
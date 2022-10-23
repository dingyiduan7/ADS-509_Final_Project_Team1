# package imports
from flask import Flask, render_template, url_for, request
import joblib
import pickle
import nltk
import re
import pandas as pd

from nltk.corpus import stopwords
from string import punctuation


# punctuation variations
punctuation = set(punctuation) # speeds up comparison

tw_punct = punctuation #- {"#"} # remove hashtags from punctuation list

# stopwords
sw = stopwords.words("english")
sw = [i.replace("'","") for i in sw]  # remove single quote from sw

# remove retweet word
sw.extend(['rt', 'retweet'])

# we don't really need the actual names of the cryptos especially
# when the hashtags are removed
sw.extend(['bitcoin', 'ethereum', 'cardano','dogecoin','shib','shiba'])


# some useful regex
whitespace_pattern = re.compile(r"\s+")
hashtag_pattern = re.compile(r"^#[0-9a-zA-Z]+")

# text cleaning functions
def remove_url(s): 
    return re.sub(r'http\S+', '', s)

def lower_case(text):
    return text.casefold()
 
def remove_punctuation(text, punct_set=tw_punct) : 
    return("".join([ch for ch in text if ch not in punct_set]))

def tokenize(text) : 
    """ Splitting on whitespace rather than the book's tokenize function. That 
        function will drop tokens like '#hashtag' or '2A', which we need for Twitter. """
    return text.split()

def remove_stop(tokens) :
    # modify this function to remove stopwords
    tokens = [i for i in tokens if not i in sw]
    return tokens


# pipeline implementation
def prepare(text, pipeline) : 
    tokens = str(text)
    
    for transform in pipeline : 
        tokens = transform(tokens)
        
    return tokens

# cleaning pipeline
crypto_pipeline1 = [remove_url, lower_case, remove_punctuation, tokenize, remove_stop]


# app functions below

app = Flask(__name__)
model = pickle.load(open('svm_model.pkl', 'rb'))


@app.route('/')
def question():
	return render_template('question.html')


@app.route('/predict', methods=['POST'])
def predict():
        if request.method == 'POST':
            message=request.form['tweet']
            data=[message]
            tweets_df["tokens"] = data.apply(prepare,pipeline=crypto_pipeline1)
            transformed = tweets_df["tokens"].apply(prepare, pipeline=crypto_pipeline1)
            prediction = model.predict(transformed)
        return render_template('answer.html', results=prediction)


if __name__ == '__main__':
	app.run(debug=True)
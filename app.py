from flask import Flask, render_template, request, Response,redirect, url_for
import re
from gensim.models import Word2Vec
app = Flask(__name__)

model = Word2Vec.load('./data/model')
def getResult(pos, neg):
    try:
        return model.most_similar(positive=pos, negative=neg)[:5]
    except:
        return []

@app.route('/')
def home():
    pos = []
    neg = []
    res = []
    query = request.args.get('query')
    if query:
        for p in query.split('+'):
            d = p.split('-')
            if len(d) > 1: neg.append(d[1].strip())
            pos.append(d[0].strip())
        res = getResult(pos, neg)

    return render_template('home.html', positive=pos, negative=neg, results=res)

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    return redirect(url_for('home', query=query))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
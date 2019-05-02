from flask import Flask, render_template, jsonify
from Facade import Facade
from common import getData


app = Flask(__name__)

def getNewData():
    data = {}
    data['initialLoad'] = predictor.population.original_load
    data['best'] = predictor.population.bestRecord[1]
    data['current'] = predictor.population.currentBest
    return data

@app.route('/')
def index():
    return render_template('index.html', value = predictor.population.original_load, best = predictor.population.bestRecord[1])
    #return render_template('index.html')

@app.route('/next')
def next():
    predictor.nextGen()
    return jsonify(getNewData())

@app.route('/data')
def teste():
    return jsonify(getNewData())

if __name__=='__main__':
    predictor = Facade(getData())
    app.run(debug=True)


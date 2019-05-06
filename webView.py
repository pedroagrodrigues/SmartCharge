from flask import Flask, render_template, jsonify, request, flash
from Facade import Facade
from common import getData


app = Flask(__name__)


def getNewData():
    data = {}
    data['initialLoad'] = app.predictor.population.original_load
    data['best'] = app.predictor.population.bestRecord[1]
    data['current'] = app.predictor.population.currentBest
    return data

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def form_post():
    plug_id = request.form['plug_id']
    startDate = request.form['startDate']
    endDate = request.form['endDate']
    offset = request.form['offset']
    app.predictor = Facade(getData(plug_id, startDate, endDate, offset))
    return render_template('index.html')

@app.route('/next')
def next():
    app.predictor.nextGen()
    return jsonify(getNewData())

@app.route('/data')
def get_Data():
    return jsonify(getNewData())


if __name__=='__main__':
    app.predictor = ''
    app.run(debug=True)


from flask import Flask, render_template
from Facade import Facade
from common import getData
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.htm', value = predictor.population.original_load)

@app.route('/about')
def about():
    return 'This is an exemple of another page'

@app.route('/teste')
def teste():
    predictor.nextGen()
    return str(predictor.population.bestRecord)

if __name__=='__main__':
    predictor = Facade(getData())
    app.run(debug=True)
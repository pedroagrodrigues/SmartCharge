from flask import Flask
from Facade import Facade
from common import getData
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a <b>\'Hello World!\'</b> I will be doing most of the work here'

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
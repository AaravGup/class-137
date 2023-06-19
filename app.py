from flask import Flask, jsonify,request,render_template
from data import data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',planets = data)

@app.route('/planet')
def planet():
    name = request.args.get('name')
    #planetData = next(item for item in data if item['name'] == name)
    for item in data:
        if item['name'] == name:
            planetData = item

    return jsonify({
        'data': planetData,
        'message': 'success'
    }),200



if __name__ == '__main__':
    app.run()
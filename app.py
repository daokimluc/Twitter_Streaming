from flask import Flask, jsonify, request, render_template
from camelcase import CamelCase
from tweet import *
import ast


c = CamelCase()

app = Flask(__name__)

labels = []
values = []


@app.route('/', methods=["GET"])
def search_country():
    return render_template('search.html')


@app.route('/trends', methods=["GET", "POST"])
def get_tweets():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
    api = authentication()
    woeid = search_woeid(api, name)
    if woeid == 1:
        name = 'Worldwide'
    data = data_fetching(api, woeid)
    clean_data = data_cleaning(data)
    return render_template('index.html', data=clean_data, name=c.hump(name))


@app.route("/streamTweets", methods=["GET", "POST"])
def chart():
    global labels, values
    labels = []
    values = []
    return render_template('chart.html', values=values, labels=labels)


@app.route('/refreshData')
def refresh_graph_data():
    global labels, values
    print("labels now: " + str(labels))
    print("data now: " + str(values))
    return jsonify(sLabel=labels, sData=values)


@app.route('/updateData', methods=['POST'])
def update_data_post():
    global labels, values
    if not request.form or 'data' not in request.form:
        return "error", 400
    labels = ast.literal_eval(request.form['label'])
    values = ast.literal_eval(request.form['data'])
    print("labels received: " + str(labels))
    print("data received: " + str(values))
    return "success", 201


if __name__ == "__main__":
    app.run(host='localhost', port=5011)

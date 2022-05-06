import flask
from flask_cors import CORS
from transformData import decodeBase64
from cnn import getPredictionCNN 
import json


app = flask.Flask(__name__)
CORS(app)

app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def getPrediction():
    return "ok"

@app.route('/check', methods=['POST'])
def getPrediction():
    decodeBase64(flask.request.json["base64"])
    data = getPredictionCNN()
    data = [data[0],data[1], data[2]]
    return json.dumps(str(data))

app.run(debug=True, use_reloader=False)
app.run(host='0.0.0.0', port=80)
app.run()


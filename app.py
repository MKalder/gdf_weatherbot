from flask import Flask
from flask import Flask, request, make_response
import json
from flask_cors import CORS,cross_origin
from weather_data import WeatherData

weather_data = WeatherData()
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    #print("Request:")
    
    #print(json.dumps(req))

    res = weather_data.processRequest(req)

    res = json.dumps(res)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)


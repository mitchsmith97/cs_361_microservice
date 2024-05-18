from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
microA_server = 'http://localhost:9923/'

@app.route('/get_completion_time', methods=['Get'])
def get_completion_time():

    fitness = 3
    distance = 50
    elevation_gain = 500
    data = {'distance': distance, 'elevation_gain': elevation_gain,'fitness': fitness}
    response = requests.post(microA_server + 'estimated_time', json=data)
    completion_time = response.json()['completion_time']
    print(completion_time)


    elevation = 2000
    distance = 1
    data2 = {'distance': distance, 'elevation_gain': elevation_gain}
    response = requests.post(microA_server + 'estimated_difficulty', json=data2)
    difficulty = response.json()['difficulty']
    print(difficulty)

    return 'Completion time: ' + str(completion_time) + '\n Estimated Difficulty: ' + str(difficulty)

if __name__ == "__main__":
    app.run(port=8742, threaded=True)
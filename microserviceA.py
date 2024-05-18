import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

#Estimates time for a hike
#Required inputs {'distance': float, 'elevation_gain': float, 'fitness': int}
#Response: {'completion_time: float}
@app.route('/estimated_time', methods=['post'])
def estimated_time():

    try:
        data = request.get_json()
        distance = float(data['distance'])
        elevation_gain = float(data['elevation_gain'])
        fitness_level = int(data['fitness'])
        
        speeds = [2, 2, 2, 2.5, 2.5, 3, 3, 3.5, 3.5, 4]
        adjustments = [500, 500, 500, 600, 600, 700, 700, 800, 800, 900]

        average_speed = speeds[fitness_level-1]
        elevation_adjustment = adjustments[fitness_level-1]

        #print(f"Received data: {data}")
        completion_time = distance/average_speed + elevation_gain/elevation_adjustment
        return jsonify({'completion_time': completion_time}), 200
    
    except:
        return 400


#Estimates difficulty of a hike
#Required inputs {'distance': float, 'elevation_gain': float}
#Response: {'difficulty': float}
@app.route('/estimated_difficulty', methods=['post'])
def estimated_difficulty():

    try:
        data = request.get_json()
        #print(f"Received data: {data}")

        distance = float(data['distance'])
        elevation_gain = float(data['elevation_gain'])

        difficulty = elevation_gain/distance/10
        
        return jsonify({'difficulty': difficulty}), 200
    
    except:
        return 400

if __name__ == "__main__":
    app.run(port=9923, threaded=True)
    
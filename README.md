# cs_361_microservice

This microservice provides a way to calculate both an estimated time a hike takes as well as an estimated difficulty of the hike. It runs on a flask server and can be accessed with http/REST post requests. 

To obtain an estimated time of a hike, call the server with a post request directed to /estimated_time. A JSON must be included containing distance, elevation gain, and fitness. Example code below:

    microA_server = 'http://localhost:9923/'
    data = {'distance': distance, 'elevation_gain': elevation_gain,'fitness': fitness}
    response = requests.post(microA_server + 'estimated_time', json=data)
    completion_time = response.json()['completion_time']

Obtaining the difficulty is very similar. The post request is directed to /estimated_difficulty, and the JSON only includes the distance and elevation gain.
    elevation = 2000
    distance = 1
    data2 = {'distance': distance, 'elevation_gain': elevation_gain}
    response = requests.post(microA_server + 'estimated_difficulty', json=data2)
    difficulty = response.json()['difficulty']

The response is in the same line of code as the request, and comes in the form of a JSON. The desired property can be extracted from the JSON, for example in the completion_time = response.json()[‘completion_time’] statement. 

![uml](https://github.com/mitchsmith97/cs_361_microservice/assets/60078133/70148ab0-968e-45ff-9366-0fd033ea606c)

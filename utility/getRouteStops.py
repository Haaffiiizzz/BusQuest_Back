import json

testRoute = "BLUE"

with open("data/main/trips.json", "r") as tripsFile, \
    open("data/main/stop_times.json", "r") as stopTimesFile, \
    open("data/main/stops.json", "r") as stopsFile, \
    open(f"data/routes/{testRoute}_stops.json", "w") as resultFile:
    #open all files at once

    allTrips = json.load(tripsFile)
    allStopTimes = json.load(stopTimesFile)
    allStops = json.load(stopsFile)

    result = []
    testRouteTrips = allTrips[testRoute]

    for trip in filter(lambda x: x["direction_id"] == "1", testRouteTrips):
        tripID = trip["trip_id"]

        for stopTime in allStopTimes[tripID]:
            stopID = stopTime["stop_id"]
            stop = allStops[stopID]

            result.append(stop)

    json.dump(result, resultFile, indent=4)











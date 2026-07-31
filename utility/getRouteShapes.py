import json

with open("data/main/trips.json", "r") as file:
    allTrips = json.load(file)

with open("data/main/stop_times.json", "r") as file:
    allStopTimes = json.load(file)


routeShapes = {}

for routeID, trips in allTrips.items():
    routeShapes[routeID] = {}

    for trip in trips:
        tripID = trip["trip_id"]
        directionID = trip["direction_id"]
        stopCount = len(allStopTimes[tripID])

        if directionID not in routeShapes[routeID]:
            routeShapes[routeID][directionID] = {
                "trip_id": tripID,
                "shape_id": trip["shape_id"],
                "stop_count": stopCount
            }
            continue

        currentBest = routeShapes[routeID][directionID]

        if stopCount > currentBest["stop_count"]:
            routeShapes[routeID][directionID] = {
                "trip_id": tripID,
                "shape_id": trip["shape_id"],
                "stop_count": stopCount
            }


with open("data/routes/route_shapes.json", "w") as file:
    json.dump(routeShapes, file, indent=4)
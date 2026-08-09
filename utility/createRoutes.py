import json


with open("data/main/routes.json", "r") as file:
    allRoutes = json.load(file)

with open("data/main/trips.json", "r") as file:
    allTrips = json.load(file)

with open("data/main/stop_times.json", "r") as file:
    allStopTimes = json.load(file)

with open("data/main/stops.json", "r") as file:
    allStops = json.load(file)


routesData = {}


for routeID, trips in allTrips.items():

    route = allRoutes[routeID]

    routesData[routeID] = {
        "route": route,
        "directions": {}
    }

    for trip in trips:

        tripID = trip["trip_id"]
        directionID = trip["direction_id"]

        stopCount = len(allStopTimes[tripID])

        if directionID not in routesData[routeID]["directions"]:
            routesData[routeID]["directions"][directionID] = {
                "trip_id": tripID,
                "shape_id": trip["shape_id"],
                "stop_count": stopCount,
                "stops": []
            }

        currentTrip = routesData[routeID]["directions"][directionID]

        if stopCount > currentTrip["stop_count"]:
            routesData[routeID]["directions"][directionID] = {
                "trip_id": tripID,
                "shape_id": trip["shape_id"],
                "stop_count": stopCount,
                "stops": []
            }


for routeID, routeData in routesData.items():

    for directionID, directionData in routeData["directions"].items():

        tripID = directionData["trip_id"]

        for stopTime in allStopTimes[tripID]:

            stopID = stopTime["stop_id"]

            directionData["stops"].append(
                allStops[stopID]
            )


with open("data/main/routes_data.json", "w") as file:
    json.dump(routesData, file, indent=4)
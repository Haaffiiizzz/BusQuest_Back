import json

testRoute = "BLUE"

# Load data
with open("data/main/trips.json", "r") as file:
    allTrips = json.load(file)

with open("data/main/stop_times.json", "r") as file:
    allStopTimes = json.load(file)

testRouteTrips = allTrips[testRoute]


# Organize shapes by direction
directionShapes = {}

for trip in testRouteTrips:
    directionID = trip["direction_id"]
    shapeID = trip["shape_id"]
    tripID = trip["trip_id"]

    stopCount = len(allStopTimes[tripID])

    if directionID not in directionShapes:
        directionShapes[directionID] = {}

    if shapeID not in directionShapes[directionID]:
        directionShapes[directionID][shapeID] = {
            "tripCount": 0,
            "maxStops": 0,
            "longestTripID": None
        }

    shape = directionShapes[directionID][shapeID]

    # Count how many trips use this shape
    shape["tripCount"] += 1

    # Keep track of the trip with the most stops
    if stopCount > shape["maxStops"]:
        shape["maxStops"] = stopCount
        shape["longestTripID"] = tripID


# Print results
for directionID, shapes in directionShapes.items():
    print(f"\nDirection {directionID}")
    print(f"Unique shapes: {len(shapes)}")

    for shapeID, data in shapes.items():
        print(
            f"Shape {shapeID}: "
            f"{data['tripCount']} trips, "
            f"max {data['maxStops']} stops, "
            f"trip {data['longestTripID']}"
        )


# Find the shape with the most stops in each direction
print("\nRepresentative shapes")

for directionID, shapes in directionShapes.items():

    longestShapeID = None
    mostStops = 0

    for shapeID, data in shapes.items():
        if data["maxStops"] > mostStops:
            mostStops = data["maxStops"]
            longestShapeID = shapeID

    print(
        f"Direction {directionID}: "
        f"Shape {longestShapeID}, "
        f"{mostStops} stops"
    )
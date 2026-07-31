import json
from pathlib import Path

uniqueHeader = ["routes", "stops"]
allHeaders = ["shapes", "stop_times", "trips", "routes", "stops"]

uniqueFiles = [ Path("data/raw gtfs") / f"{name}.txt" for name in uniqueHeader] #files where we can use the first column as key since they are all unique
allFiles = [Path("data/raw gtfs") / f"{name}.txt" for name in allHeaders]


for file in allFiles:
    with open(file, "r") as txtFile:
        txtFile = txtFile.readlines()
        headers = txtFile[0].split(",")[1:] #all other headers asides first one

        newDict = {}

        n = len(headers)
        for line in txtFile[1:]:
            lineList = line.split(",")

            if file in uniqueFiles:
                newDict[lineList[0]] = {headers[i].strip(): lineList[i+1].strip() for i in range(n)}

            else:
                if lineList[0] in newDict:
                    newDict[lineList[0]].append({headers[i].strip(): lineList[i+1].strip() for i in range(n)})
                else:
                    newDict[lineList[0]] = [{headers[i].strip(): lineList[i+1].strip() for i in range(n)}]

        outputFile = Path("data/main") / file.with_suffix(".json").name

        with open(outputFile, "w") as newFile:
            json.dump(newDict, newFile, indent=4)

import json
from pathlib import Path

files = list(Path("data/main").glob("*.txt"))

for file in files:
    with open(file, "r") as txtFile:
        txtFile = txtFile.readlines()
        headers = txtFile[0].split(",")[1:] #all other headers asides first one

        newDict = {}

        n = len(headers)
        for line in txtFile[1:]:
            lineList = line.split(",")
            newDict[lineList[0]] = {headers[i].strip(): lineList[i+1].strip() for i in range(n)}

        with open(str(file).strip(".txt")+".json", "w") as newFile:
            json.dump(newDict, newFile, indent=4)
#this only works for csv with unique first header
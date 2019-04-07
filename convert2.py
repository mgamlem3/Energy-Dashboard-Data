import os
import csv
import json

fieldnames = ("Week Ending", "Weekly Consumption", "Peak Demand", "Peak Time")

jsonFiles = dict()

for root, dirs, files in os.walk("./energylogs"):
    for file in files:
        try:
            currentBuilding = file.split()[0]
            if "EnergyLog" in currentBuilding:
                continue

            jsonFile = jsonFiles.get(currentBuilding, None)
            if jsonFile is None:
                try:
                    jsonFile = open("{}.json".format(currentBuilding), 'w')
                except Exception as e:
                    print("{}: ".format(e) + os.path.join(root, file))
                jsonFiles[currentBuilding] = jsonFile.name
            else:
                try:
                    jsonFile = open(jsonFile, 'w')
                except:
                    print("error: " + os.path.join(root, jsonFile))

            # read csv
            try:
                if os.path.getsize(os.path.join(root, file)) is 0:
                    continue

                readCSV = csv.DictReader(open(os.path.join(root, file)), delimiter=',')
                for row in readCSV:
                    json.dump(row, jsonFile)
                    print(row)
                file.close()

            except (csv.Error):
                print("Unknown CSV Error")
                continue

        except:
            continue
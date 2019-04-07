# !/usr/bin/python3

import os
import csv
import json

jsonOut = open("out.json", 'w')
fieldnames = ("     Week     Ending ", "Weekly Consumption", "Peak Demand", "Peak Time")

# file = open("./energylogs/2019/Mar/Aquatics Energy Logging Report_DY-W-2019-03-02.csv", "r")
for root, dirs, files in os.walk("./energylogs"):
    for file in files:
        try:
            # print("Evaluating: " + os.path.join(root, file))
            currentFile = open(os.path.join(root, file))
            readCSV = csv.DictReader(currentFile, fieldnames)
            for row in readCSV:
                if row is not currentFile.name:
                    json.dump(row, jsonOut)
                    print(row)
                    jsonOut.write(',\n')
            currentFile.close()
        except (csv.Error):
            continue
        except:
            continue

jsonOut.close()

print("Done")
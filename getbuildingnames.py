import os
import pandas
import requests
buildings = {}

for root, dirs, files in os.walk("./energylogs"):
    for file in files:
        try:
            currentBuilding = file.split()[0]
            if "EnergyLog" in currentBuilding:
                continue

            # add to dict
            if not currentBuilding in buildings.keys():
                buildings[currentBuilding] = 1
            else:
                buildings[currentBuilding] = buildings[currentBuilding] + 1

            # # read csv
            # try:
            #     if os.path.getsize(os.path.join(root, file)) is 0:
            #         continue
                
            #     # add building
            #     df = pandas.read_csv(os.path.join(root, file))
            #     df['Building'] = currentBuilding

            # except Exception as e:
            #     print(e)
        except Exception as e:
            print(e)

print(buildings.keys())

# dict_keys(['All', 'Boppel', 'McMillin', 'Warren', 'McEachran', 'Field', 'Aquatics', 'HUB', 'Westminster', 'Cowles', 'Chapel', 'Scotford', 'Duvall', 'Weyerhaeuser', 'Hendrick', 'Visual', 'Johnston', 'Library', 'l', 'Rec', 'Lindaman'])
import os
import pandas
import requests
import re

buildings = {
    "Aquatics",
    "Arend",
    "Auld",
    "Baldwin-Jenkins",
    "Ballard",
    "Chapel",
    "Boppel",
    "Auditorium",
    "Library",
    "Music Building",
    "Dixon",
    "Duvall",
    "Eric Johnston",
    "Facilities",
    "Fieldhouse",
    "Grahm",
    "Graves",
    "Hardwick",
    "Hawthorne",
    "Hendrick",
    "Hill House",
    "HUB",
    "Leid",
    "Lindaman",
    "MacKay",
    "McEachran",
    "McMillan",
    "East",
    "Robinson",
    "Schumacher",
    "Stewart",
    "Tacoma",
    "Tennis Bubble",
    "University Recreation Center",
    "The Village (Akili)",
    "The Village (Shalom)",
    "The Village (Tiki)",
    "Warren",
    "Westminster",
    "Weyerhaeuser"
}

for root, dirs, files in os.walk("./trendlog"):
    for file in files:
        try:
            for name in buildings:
                if name in file:
                    currentBuilding = name
            if "EnergyLog" in currentBuilding:
                continue

            # read csv
            try:
                if os.path.getsize(os.path.join(root, file)) is 0:
                    continue
                
                # add building
                df = pandas.read_csv(os.path.join(root, file))
                df['Building'] = currentBuilding

                # convert dataframe to dict
                dict_df = df.to_dict()
                # temp to store data before post
                try:
                    i = 0
                    while i < len(dict_df):
                        if "Time" in dict_df:
                            values = list(dict_df)
                            data = {
                                'date' : dict_df['Time'][i],
                                'weeklyConsumption' : 0,
                                'peakDemand' : dict_df[values[1]][i],
                                'buildingName' : dict_df['Building'][i],
                                'peakTime' : 0,
                            }

                            # post to database
                            req = requests.post(url='http://localhost:5001/api/putData', data=data, headers={'content-type': 'application/x-www-form-urlencoded'})

                            print(req.status_code)
                        else:
                            pass
                        i += 1
                except Exception as e:
                    print(e)
                    pass

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


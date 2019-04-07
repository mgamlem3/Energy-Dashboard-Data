import os
import pandas
import requests

for root, dirs, files in os.walk("./energylogs"):
    for file in files:
        try:
            currentBuilding = file.split()[0]
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
                    if "     Week     Ending " in dict_df:
                        data = {
                            'date' : dict_df['     Week     Ending '][0],
                            'weeklyConsumption' : dict_df['Weekly Consumption'][0],
                            'peakDemand' : dict_df['Peak Demand'][0],
                            'buildingName' : dict_df['Building'][0],
                            'peakTime' : dict_df['Peak Time'][0],
                        }
                    else:
                        pass
                except Exception as e:
                    print(e)
                    pass

                # add first line of data to dataframe
                # for key in dict_df.keys():
                #     data[key.strip()] = dict_df[key][0]

                # post to database
                req = requests.post(url='http://localhost:5001/api/putData', data=data, headers={'content-type': 'application/x-www-form-urlencoded'})

                print(req.status_code)

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


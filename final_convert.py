import os
import pandas
import json
import pymongo

mainDataframe = pandas.DataFrame()

# ====== Connection ====== #
# Connection to Mongo
my_client = pymongo.MongoClient('127.0.0.1',27017)
# Connection to the database
db = my_client["energy-dashboard"]
# Connection to the collection
collection = db["data"]

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
                
                df = pandas.read_csv(os.path.join(root, file))
                df['Building'] = currentBuilding

                mainDataframe = mainDataframe.append(df.iloc[0], ignore_index=True)
                
                # Try insert
                # collection.insert_one(df.to_dict())
                records = json.loads(df.T.to_json()).values()
                collection.insert(records)

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

# delete null rows
try:
    data_json = json.loads(df.to_json(orient='records'))
except Exception as e:
    print(e)
# mainDataframe.dropna(inplace=True)

# try:
#     jsonOut = open('out.json', 'w')
# except:
#     print('Error while writing to file.')

# jsonOut.write(str(mainDataframe))

# jsonOut.close()

# data = mainDataframe.to_json(orient='records')

# json.dumps(data, indent=4, sort_keys=True)
# json.dump(data, jsonOut)

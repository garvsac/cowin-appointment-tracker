import requests
import datetime
import json
import pandas as pd

#for state_code in range(1,40):
#    print("State code: ", state_code)
#    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code))
#    json_data = json.loads(response.text)
#    for i in json_data["districts"]:
#        print(i["district_id"],'\t', i["district_name"])
#    print("\n")

DIST_ID = [664,663]
#663 	 Kanpur Dehat
#664 	 Kanpur Nagar
Age = 18

base = datetime.datetime.today()
date_str = base.strftime("%d-%m-%Y")

#print(json.dumps(resp_json, indent = 1))

for dist in DIST_ID:
    print(dist)
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(dist, date_str)
    response = requests.get(URL)
    if response.ok:
        resp_json = response.json()
        if resp_json["centers"] :
            for center in resp_json["centers"]:
                for session in center["sessions"]:
                    #print( session["date"] ,center["name"] + ":", session["available_capacity"] )
                    if( session["min_age_limit"] == 18 ):
                        print( session["date"] ,center["name"] + ":", session["available_capacity"] )
                        if( session["available_capacity"] > 0 ):
                            print("You can book vaccine slots on {}".format(date_str))
        else:
            print("No available slots on {}".format(date_str))

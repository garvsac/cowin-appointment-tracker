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
DIST_ID = 663
print_flag = 'n'
Age = 18

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(1)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
print(date_str)

for INP_DATE in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, INP_DATE)
    response = requests.get(URL)
    if response.ok:
        resp_json = response.json()
        if resp_json["centers"] :
            for center in resp_json["centers"]:
                print( center["name"] )
                for session in center["sessions"]:
                    if( session["min_age_limit"] == 18 ):
                        print( session["available_capacity"] )
            print("You can book vaccine slots on {}".format(INP_DATE))
            if(print_flag=='y' or print_flag=='Y'):
                print(json.dumps(resp_json, indent = 1))
        else:
            print("No available slots on {}".format(INP_DATE))

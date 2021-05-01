import requests
import datetime
import json
import pandas as pd
#print(json.dumps(resp_json, indent = 1))

DIST_ID = [664,663]
#663 	 Kanpur Dehat
#664 	 Kanpur Nagar
Age = 18

base = datetime.datetime.today()
date_str = base.strftime("%d-%m-%Y")

#use this to setup alerts on phone https://betterprogramming.pub/how-to-send-push-notifications-to-your-phone-from-any-script-6b70e34748f6
urlNotif = 'https://maker.ifttt.com/trigger/notify/with/key/d4XdotM5gAlYHatbEqyRMXdiTPVP-2BFAzRTrK7jr3q'

for dist in DIST_ID:
    print(dist)
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(dist, date_str)
    response = requests.get(URL)
    if response.ok:
        resp_json = response.json()
        if resp_json["centers"] :
            for center in resp_json["centers"]:
                for session in center["sessions"]:
                    if( session["min_age_limit"] == 18 ):
                        #print( session )
                        Message = "{}: {} - {}".format( session["date"] ,center["name"], session["available_capacity"] )
                        print( Message )
                        if( session["available_capacity"] > 0 ):
                            print("Available", Message)
                            myobj = {"value1":Message}
                            notif = requests.post(urlNotif, data = myobj)
                            #print(notif.text)

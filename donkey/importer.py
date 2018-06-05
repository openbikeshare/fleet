import requests
import cycle_location

class DonkeyRepublicImporter():
    def __init__(self, token):
        self.url = 'https://stables.donkey.bike/api/public/availability/hubs'
        self.token = token

    def import_bike(self, feed, bike):
        return cycle_location.CycleLocation(feed + ':' + str(bike["id"]), bike["latitude"], bike["longitude"], feed, "station", None)

    def import_json(self, feed, json):
        cycles = []
        for bike in json:
            cycles.append(self.import_bike(feed, bike))
        return cycles

    def import_feed(self):
        cycles = []
        payload = {'location': '52.160105,5.382660', 'radius': '100000'}
        headers = {'X-Api-Key': self.token, 'Accept': 'application/com.donkeyrepublic.v2'}
        r = requests.get(self.url, params=payload, headers=headers)
        return self.import_json("donkey", r.json())

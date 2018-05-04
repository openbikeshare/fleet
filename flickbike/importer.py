import requests
import cycle_location

class FlickBikeImporter():
    def __init__(self, url):
        self.url = url

    def import_bike(self, feed, bike):
        return cycle_location.CycleLocation(feed + ':' + bike["bid"], bike["gLat"], bike["gLng"], feed, "bike", None)

    def import_json(self, feed, json):
        cycles = []
        for bike in json["data"]:
            cycles.append(self.import_bike(feed, bike))
        return cycles

    def import_feed(self):
        cycles = []
        r = requests.get(self.url)
        return self.import_json("flickbike", r.json())

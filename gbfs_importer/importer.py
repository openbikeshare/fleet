import requests
import cycle_location
from .free_bike_status_importer import FreeBikeStatusImporter

class GbfsImporter():
    def __init__(self):
        self.feeds = [{'operator': 'nextbike', 'url': 'https://api.nextbike.net/maps/gbfs/v1/nextbike_nl/gbfs.json'},
                {'operator': 'nextbike', 'url': 'https://api.nextbike.net/maps/gbfs/v1/nextbike_nd/gbfs.json'}] 

    def import_station(self, operator, station, last_updated):
        return cycle_location.CycleLocation(operator + ':' + station["station_id"], station["lat"],
            station["lon"], operator, "station", last_updated)

    def import_station_json(self, operator, json):
        cycles = []
        print(json)
        for station in json["data"]["stations"]:
            cycles.append(self.import_station(operator, station, json["last_updated"]))
        return cycles

    def import_json(self, operator, json):
        cycles = []
        free_bike_status_import = FreeBikeStatusImporter(operator)
        if json["data"]["en"]["feeds"]:
            for feed in json["data"]["en"]["feeds"]:
                if feed["name"] == "station_information":
                    r = requests.get(feed["url"])
                    cycles += self.import_station_json(operator, r.json())
                if feed["name"] == "free_bike_status":
                    r = requests.get(feed["url"])
                    cycles += free_bike_status_import.import_free_bike_status_json(r.json())
                    print(cycles)
        return cycles 

    def import_feed(self):
        cycles = []
        for feed in self.feeds:
            r = requests.get(feed['url'])
            cycles += self.import_json(feed['operator'], r.json())
        return cycles

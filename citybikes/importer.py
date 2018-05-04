import requests
import cycle_location

class CityBikesImporter():
    def __init__(self):
        self.feeds = [{'operator': 'cykl', 'url': 'https://api.citybik.es/v2/networks/cykl'},
                {'operator': 'nextbike_rotterdam', 'url': 'https://api.citybik.es/v2/networks/nextbike-rotterdam'},
                {'operator': 'nextbike_maastricht', 'url': 'https://api.citybik.es/v2/networks/nederland-maastricht'},
                {'operator': 'nu-connect', 'url': 'https://api.citybik.es/v2/networks/nu-connect'}] 

    def import_station(self, feed, station):
        return cycle_location.CycleLocation(feed + ':' + station["id"], station["latitude"],
            station["longitude"], feed, "station", station["timestamp"])

    def import_json(self, feed, json):
        cycles = []
        for station in json["network"]["stations"]:
            cycles.append(self.import_station(feed, station))
        return cycles

    def import_feed(self):
        cycles = []
        for feed in self.feeds:
            r = requests.get(feed['url'])
            cycles += self.import_json(feed['operator'], r.json())
        return cycles

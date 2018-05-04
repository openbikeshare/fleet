import requests
import cycle_location

class OVFietsImporter():

    def import_station(self, id, station):
        id = "ovfiets:" + id
        return cycle_location.CycleLocation(id, station["lat"],
            station["lng"], "ovfiets", "station", station["extra"]["fetchTime"])

    def import_json(self, json):
        cycles = []
        for station in json["locaties"]:
            cycles.append(self.import_station(station, json["locaties"][station]))
        return cycles

    def import_feed(self):
        r = requests.get("http://fiets.openov.nl/locaties.json")
        return self.import_json(r.json())

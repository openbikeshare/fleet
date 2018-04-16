import requests
import cycle_location

def import_station(id, station):
    id = "ovfiets:" + id
    return cycle_location.CycleLocation(id, station["lat"],
        station["lng"], station["extra"]["fetchTime"])

def import_json(json):
    cycles = []
    for station in json["locaties"]:
        cycles.append(import_station(station, json["locaties"][station]))
    return cycles

def import_feed():
    r = requests.get("http://fiets.openov.nl/locaties.json")
    return import_json(r.json())

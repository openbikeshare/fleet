import requests
import cycle_location

def import_station(station):
    return cycle_location.CycleLocation(station["id"], station["latitude"],
        station["longitude"], station["timestamp"])

def import_json(json):
    cycles = []
    for station in json["network"]["stations"]:
        cycles.append(import_station(station))
    return cycles

feeds = [{'operator': 'cykl', 'url' 'https://api.citybik.es/v2/networks/cykl'},
        {'operator': 'nextbike', 'url': ''},
        {'operator': 'nextbike', 'url': ''}] 
 
def import_feeds():
    for feed in feeds:
        r = requests.get(feed['url'])
        import_json(feed['operator', r.json())

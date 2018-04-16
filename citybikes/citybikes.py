import cycle_location


def import_feeds():
    r = requests.get("https://api.citybik.es/v2/networks/cykl")
    print(r.json())
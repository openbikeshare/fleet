import citybikes.importer
import ovfiets.importer
import time
import psycopg2

try:
    conn = psycopg2.connect("dbname='dfiets_data'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

cur.execute("DELETE FROM cycle_location")

importers = [
    citybikes.importer.CityBikesImporter(),
    ovfiets.importer.OVFietsImporter()
]

while True:
    cycle_locations = []
    cur.execute("DELETE FROM cycle_location")
    for importer in importers:
        cycle_locations += importer.import_feed()
    list(map(lambda cycle_location: cycle_location.save(cur), cycle_locations))
    conn.commit()
    print("completed")
    time.sleep(60)

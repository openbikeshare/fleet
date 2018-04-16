import citybikes.importer
import ovfiets.importer
import time
import psycopg2

try:
    conn = psycopg2.connect("dbname='dfiets_data'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

cur.execute("DELETE FROM cycle_location");

importers = [
    citybikes.importer.CityBikesImporter(),
    ovfiets.importer.OVFietsImporter()
]


while True:
    cycles = []
    cur.execute("DELETE FROM cycle_location");
    for importer in importers:
        cycles += importer.import_feed()
    list(map(lambda cycle: cycle.save(cur), cycles))
    conn.commit()
    print("completed")
    time.sleep(60)

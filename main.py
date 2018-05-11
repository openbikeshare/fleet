import citybikes.importer
import ovfiets.importer
import flickbike.importer
import cacher.cacher
import time
import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

importers = [
    citybikes.importer.CityBikesImporter(),
    ovfiets.importer.OVFietsImporter(),
    flickbike.importer.FlickBikeImporter(config['flickbike']['url'])
]

try:
    conn = psycopg2.connect("dbname='openbikeshare_data'")
except:
    print("Unable to connect to the database")

cacher = cacher.cacher.Cacher(conn)
cur = conn.cursor()

while True:
    cycle_locations = []
    cur.execute("DELETE FROM cycle_location")
    for importer in importers:
        cycle_locations += importer.import_feed()
    list(map(lambda cycle_location: cycle_location.save(cur), cycle_locations))
    conn.commit()
    print("Completed import.")
    cacher.cache()
    print("Completed caching.")
    time.sleep(60)

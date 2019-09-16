import citybikes.importer
import ovfiets.importer
import flickbike.importer
import donkey.importer
import gbfs_importer.importer
import cacher.cacher
import time
import psycopg2
import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

importers = [
    citybikes.importer.CityBikesImporter(),
    ovfiets.importer.OVFietsImporter(),
    flickbike.importer.FlickBikeImporter(os.environ['FLICKBIKE_URL']),
    donkey.importer.DonkeyRepublicImporter(os.environ['DONKEY_TOKEN']),
    gbfs_importer.importer.GbfsImporter()
]

conn_str = None
if os.environ.get("PRODUCTION") == True:
    conn_str = "postgresql://openbike:%s@%s" % (os.getenv("DB_PASSWORD"), os.getenv("DB_URL"))
else:
    conn_str = "dbname='openbikeshare_data'"
try:
    conn = psycopg2.connect(conn_str)
except:
    print("Unable to connect to the database")

cacher = cacher.cacher.Cacher(conn)


def import_bikes(conn):
    cycle_locations = []
    cur = conn.cursor()
    cur.execute("DELETE FROM cycle_location")
    for importer in importers:
        cycle_locations += importer.import_feed()
    list(map(lambda cycle_location: cycle_location.save(cur), cycle_locations))
    conn.commit()
    print("Completed import.")
    cacher.cache()
    print("Completed caching.")

while True:
    start = time.time()
    import_bikes(conn)
    delta = start - time.time()
    if delta < 60:
        time.sleep(60 - delta)
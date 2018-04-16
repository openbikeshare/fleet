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
while True:
    cycles = citybikes.importer.import_feeds()
    cycles = cycles + (ovfiets.importer.import_feed())
    list(map(lambda cycle: cycle.save(cur), cycles))
    conn.commit()
    print("completed")
    time.sleep(60)
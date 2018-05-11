import redis

class Cacher():
    def __init__(self, conn):
        self.conn = conn
        self.r = redis.Redis()

    def cache_coverage(self):
        query = """
        SELECT ST_AsGeoJSON(ST_UNION(geometry(q1.buffered))) 
        FROM (
            SELECT ST_Buffer(location, 500) as buffered 
            FROM cycle_location ) 
        as q1"""
        cur = self.conn.cursor()
        cur.execute(query)
        coverage_json = cur.fetchone()[0]
        self.r.set("coverage", coverage_json)

    def cache(self):
        self.cache_coverage()

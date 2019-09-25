
class Cacher():
    def __init__(self, conn):
        self.conn = conn

    def cache_coverage(self):
        query = """
        SELECT ST_AsGeoJSON(ST_UNION(geometry(q1.buffered))) 
        FROM (
            SELECT ST_Buffer(location, 200) as buffered 
            FROM cycle_location ) 
        as q1"""
        cur = self.conn.cursor()
        cur.execute(query)
        coverage_json = cur.fetchone()[0]
        cur.close()
        self.cache_in_db(coverage_json)

    def cache_in_db(self, coverage_json):
        cur = self.conn.cursor()
        query = """
        UPDATE CACHE
        SET attributes = attributes || hstore(ARRAY[['coverage', %s]])
        WHERE id = 1"""
        cur.execute(query, (str(coverage_json),))
        self.conn.commit()

    def cache(self):
        self.cache_coverage() 

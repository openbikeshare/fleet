class CycleLocation:
    def __init__(self, id, latitude, longitude, last_time_updated):
        self.id = id
        self.latitude = latitude 
        self.longitude = longitude
        self.last_time_updated = last_time_updated

    def save(self, cur):
        cur.execute("INSERT INTO cycle_location (id, location, type, last_time_updated) VALUES (%s, ST_SetSRID(ST_Point(%s, %s),4326), %s, now());" 
            , (self.id, self.longitude, self.latitude, "station"))
        return self

    def update(self, cur):
        cur.execute("UPDATE cycle_location SET last_time_updated = %s", self.last_time_updated)


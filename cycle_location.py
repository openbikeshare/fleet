class CycleLocation:
    def __init__(self, id, latitude, longitude, system_id, location_type, last_time_updated):
        self.id = id
        self.latitude = latitude 
        self.longitude = longitude
        self.location_type = location_type 
        self.system_id = system_id
        self.last_time_updated = last_time_updated

    def save(self, cur):
        cur.execute("INSERT INTO cycle_location (id, location, type, system_id, last_time_imported) VALUES (%s, ST_SetSRID(ST_Point(%s, %s),4326), %s, %s, now());" 
            , (self.id, self.longitude, self.latitude, self.location_type, self.system_id))
        return self

    def update(self, cur):
        cur.execute("UPDATE cycle_location SET last_time_updated = %s", self.last_time_updated)


import cycle_location

class FreeBikeStatusImporter():
    def __init__(self, operator):
        self.operator = operator

    def import_free_bike_status(self, cycle, last_updated):
        print(cycle["bike_id"])
        return cycle_location.CycleLocation(self.operator + ':' + cycle["bike_id"], cycle["lat"],
                            cycle["lon"], self.operator, "bike", last_updated)

    def import_free_bike_status_json(self, json):
        cycles = []
        for cycle in json["data"]["bikes"]:
            cycles.append(self.import_free_bike_status(cycle, json["last_updated"]))
        return cycles

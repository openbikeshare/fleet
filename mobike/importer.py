# Mobike for now has a seperate importer because they don't provide an GBFS index file yet.
# This class can also be used for other implementations of GBFS+ where the index file is missing.

import requests
import gbfs_importer

class MobikeImporter:
    def __init__(self, url):
        self.url = url
        self.importer = gbfs_importer.free_bike_status_importer.FreeBikeStatusImporter("mobike")

    def import_feed(self):
        r = requests.get(self.url)
        print(r.json())
        return self.importer.import_free_bike_status_json(r.json())

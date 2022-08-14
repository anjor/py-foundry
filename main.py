from foundry.services.multipass.multipass import Multipass
from foundry.services.phonograph2.table_storage_service import TableStorageService

multipass = Multipass("/Users/anjor/.py-foundry.json")
phonograph = TableStorageService("/Users/anjor/.py-foundry.json")

print(multipass.get_me())
print(phonograph.get_events("ri.phonograph2.main.table.ac6ad9cf-78d1-482b-9d00-ed9c31ba0097"))
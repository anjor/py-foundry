from foundry.services.multipass.multipass import Multipass
from foundry.services.phonograph2.table_storage_service import TableStorageService

multipass = Multipass("/Users/anjor/.py-foundry.json")
#phonograph = TableStorageService("/Users/anjor/.py-foundry.json")

#print(multipass.get_me())
#print(phonograph.get_events("ri.phonograph2.main.table.ac6ad9cf-78d1-482b-9d00-ed9c31ba0097", paging_token=5, page_size=2))
#print(phonograph.get_rows("ri.phonograph2.main.table.ac6ad9cf-78d1-482b-9d00-ed9c31ba0097", get_rows_request={"getRowsRequest":{"primaryKeys":[{"preference_id":"94e516bb-fd23-41fc-a8d4-f97cba06b50b"},{'preference_id': '045dc8f5-5682-486d-a618-9ad731477aaa'}]}}))
print(multipass.get_operations(["ri.compass.main.tag.b587cd64-9f68-45c9-acda-b792d5b44073"]))
print(multipass.get_operations(rids=["ri.compass.main.tag.b587cd64-9f68-45c9-acda-b792d5b44073"],operations=["compass:tags:edit-tag"]))

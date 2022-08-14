from foundry.services.phonograph2.phonograph2 import Phonograph2Service


class TableStorageService(Phonograph2Service):
    def get_events(self, table_rid, paging_token=None, paging_size=None):
        return self._json(method="GET", url="/storage/edits/tables/{tableRid}/events".format(tableRid=table_rid))
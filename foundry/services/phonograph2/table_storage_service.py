import urllib3.util

from foundry.services.phonograph2.phonograph2 import Phonograph2Service
import urllib


class TableStorageService(Phonograph2Service):
    def get_events(self, table_rid, paging_token=None, page_size=None):
        params = {"pagingToken": paging_token, "pageSize": page_size}
        return self._json(
            method="GET",
            url="/storage/edits/tables/{tableRid}/events".format(tableRid=table_rid),
            params=params
        )

    def get_rows(self, table_rid, get_rows_request, expected_table_schema_version=None):
        params = {"expectedTableSchemaVersion": expected_table_schema_version}
        return self._json(
            method="POST",
            url="/storage/load/tables/{tableRid}".format(tableRid=table_rid),
            params=params,
            json=get_rows_request
        )
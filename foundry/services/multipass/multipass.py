from foundry.services.abstract_service import AbstractService


class Multipass(AbstractService):
    def __init__(self, config_file):
        super().__init__(config_file)
        self._api_root = "/multipass/api"

    def get_me(self):
        return self._json(method="GET", url="/me")

    def get_operation(self, rid):
        return self._json(
            method="GET",
            url="/authz/operations/{rid}".format(rid=rid)
        )

    def get_operations(self, rids, operations=None):
        params = {"operations": operations}
        return self._json(
            method="POST",
            url="/authz/batch/operations",
            params=params,
            json=rids
        )

    def is_operation_shared(self, rid, other_user_id, operation):
        params = {"otherUserId": other_user_id, "operation": operation}
        return self._json(
            method="GET",
            url="/authz/shared/{rid}/isOperationShared".format(rid=rid),
            params=params
        )

    def get_shared_operations(self, rid, other_user_id, operation_mask):
        params = {"otherUserId": other_user_id, "operationMask": operation_mask}
        return self._json(
            method="GET",
            url="/authz/shared/{rid}/getSharedOperations".format(rid=rid),
            params=params
        )

    def detailed_has_operations(self, rid, operations):
        params = {"operations": operations}
        return self._json(
            method="GET",
            url="/authz/access/detailed/{rid}".format(rid=rid),
            params=params
        )

    def has_operations(self, rid, operations):
        params = {"operations": operations}
        return self._json(
            method="GET",
            url="/authz/access/{rid}".format(rid=rid),
            params=params
        )

    def has_operations_batch(self, rids, operations):
        params = {"operations": operations}
        return self._json(
            method="GET",
            url="/authz/batch/access",
            params=params,
            json=rids
        )

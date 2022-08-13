from foundry.services.abstract_service import AbstractService


class Multipass(AbstractService):
    def __init__(self, config_file):
        super().__init__(config_file)
        self._api_root = "/multipass/api"

    def get_me(self):
        return self._json(method="GET", url="/me")

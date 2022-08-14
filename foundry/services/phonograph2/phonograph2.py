from foundry.services.abstract_service import AbstractService


class Phonograph2Service(AbstractService):
    def __init__(self, config_file):
        super().__init__(config_file)
        self._api_root = "/phonograph2/api"


import requests

from foundry.config.config import Config


class AbstractService(object):
    def __init__(self, config_file):
        self._api_root = ""
        self._config = Config(config_file)

    def _request(self, method="GET", **kwargs):
        kwargs = self._prepare_request(kwargs)
        response = requests.request(method=method, **kwargs)
        return response

    def _json(self, method, **kwargs):
        request = self._request(method, **kwargs)
        # To do: add error handling
        return request.json()

    def _prepare_request(self, kwargs):
        kwargs = self._prepare_url(kwargs)
        kwargs['headers'] = self._prepare_auth()

        return kwargs

    def _prepare_url(self, kwargs):
        assert 'url' in kwargs, "url not set in options"
        kwargs['url'] = self._config.host + self.api_root + kwargs['url']
        return kwargs

    def _prepare_auth(self):
        return {"Authorization": "Bearer " + self._config.token}

    @property
    def api_root(self):
        print(self._api_root)
        return self._api_root

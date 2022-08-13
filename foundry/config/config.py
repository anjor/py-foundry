import json


def _parse_json_file(json_file):
    f = open(json_file)
    conf = json.load(f)
    f.close()

    return conf


class Config(object):
    def __init__(self, json_file):
        conf = _parse_json_file(json_file)
        self._host = conf['host']
        self._token = conf['token']

    @property
    def host(self):
        return self._host

    @property
    def token(self):
        return self._token
import json


class Configs:
    def __init__(self):
        self._db = {}
        self._categories = []
        self._slack_channels = []
        self._print_to_slack = False
        self._server_port = 5001

        self._read_config_file()


    def _read_config_file(self):
        print 'Reading config file...'
        with open('config.json') as data_file:
            data = json.load(data_file)

            if 'db' in data:
                self._db = data['db']

            if 'categories' in data:
                self._categories = data['categories']

            if 'slack_channels' in data:
                self._slack_channels = data['slack_channels']

            if 'print_to_slack' in data:
                self._print_to_slack = data['print_to_slack']

            if 'server_port' in data:
                self._server_port = data['server_port']


    def get_db(self):
        return self._db


    def get_categories(self):
        return self._categories


    def get_slack_channels(self):
        return self._slack_channels


    def get_print_to_slack(self):
        return self._print_to_slack


    def get_server_port(self):
        return self._server_port

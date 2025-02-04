from datetime import datetime
import requests
from requests.structures import CaseInsensitiveDict
import json


class Plugin:
    @staticmethod
    def process(self, config, alarm_data):
        url = "https://www.divera247.com/api/alarm"
        api_key = config['Divera']['api_key']

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        data = {
            "title": alarm_data['keyword'],
            "text": alarm_data['text'],
            "address": self.get_address(alarm_data),
            "ric": ','.join(alarm_data['ric_list']),
            "accesskey": api_key,
        }

        print(json.dumps(data, ensure_ascii=False))

        resp = requests.post(url, headers=headers, data=json.dumps(data))
        print(resp.status_code)
        print(resp.content)

    @staticmethod
    def get_address(alarm_data):
        return '{0} {1}, {2}'.format(alarm_data['street'], alarm_data['house_number'], alarm_data['city'])


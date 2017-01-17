from datetime import datetime
import json

import requests


SINGLE_MEASURE = 'single_measurement'
TIME_SERIES = 'time_series'


class Client(object):
    """Client for making requests to the Interana external api"""

    def __init__(self, host, token):
        self.host = host
        self.token = token
        self._verify_certs = True

    def query(self, query_obj):
        """Makes a request to the query api endpoint. Expects a Query object"""

        uri = 'https://{0}/api/v1/query'.format(self.host)
        headers = {
            'Authorization': 'Token {0}'.format(self.token)
        }
        params = {
            'query': query_obj.get_params()
        }
        response = requests.get(
            uri,
            params=params,
            headers=headers,
            verify=self._verify_certs
        )
        if response.status_code != 200:
            raise InteranaError(response.status_code, response.json())
        return Result(query_obj.get_type(), response.json())


class Query(object):

    def __init__(self, dataset, start, end, **kwargs):
        self.params = {}
        self.params['dataset'] = dataset

        # start and end times can be passed as an int or a datetime
        self.params['start'] = self.convert_to_millis(start)
        self.params['end'] = self.convert_to_millis(end)

        self.params['queries'] = []
        self.params.update(kwargs)

    def convert_to_millis(self, time):
        """Converts datetime objects to milliseconds since epoch"""

        if not isinstance(time, datetime):
            return time

        delta = time - datetime(1970, 1, 1)
        return int(delta.total_seconds() * 1000)

    def get_params(self):
        return json.dumps(self.params)

    def get_type(self):
        queries = self.params.get('queries')
        if not queries:
            return None

        return queries[0]['type']

    def add_params(self, **kwargs):
        self.params.update(kwargs)

    def add_query_info(self, type, aggregator, column=None, filter=None):
        """Add query info to the Query. Currently, only one set of query
        info can be added
        """
        query = {
            'type': type,
            'measure': {
                'aggregator': aggregator,
                'column': column
            },
            'filter': filter
        }
        self.params['queries'].append(query)


class Result(object):

    def __init__(self, type, response):
        self.type = type
        self._response = response
        self.columns = response['columns']
        self.rows = response['rows']

    def __str__(self):
        return str(self._response)

    def get_labels(self):
        return [column['label'] for column in self.columns]

    def get_formatted_labels(self):
        """Returns a list of labels where labels consisting of
        multiple entries are concatenated with comma separators
        """
        return [label if isinstance(label, basestring) else ', '.join(label)
                for label in self.get_labels()]

    def get_timestamps(self):
        """For time_series queries, returns a list of datetimes
        corresponding to the timestamps of the data points in the result
        """
        if self.type != TIME_SERIES:
            return []

        # datetime.fromtimestamp will convert the timestamp to the platform's
        # local date and time
        return [datetime.fromtimestamp(value['timestamp'] / 1000)
                for value in self.rows[0]['values'][1]]


class InteranaError(Exception):

    def __init__(self, code, response):
        self.code = code
        self.error = response.get('error')
        self.message = response.get('message')

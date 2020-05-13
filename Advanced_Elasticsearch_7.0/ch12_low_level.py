#!/usr/bin/python3

'''
initialize a low-level client with a hostname or address, a port, and parameters such as maximum connections, maxsize . The getInstance() method call returns the singleton client. With the following code block, you can obtain a low-level client running on the localhost with port=9200 and maxsize=25
'''

from elasticsearch import Elasticsearch
import threading, unittest

class ESLowLevelClient:
    __es = None
    __es_lock = threading.Lock()

    @staticmethod
    def get_instance():
        if ESLowLevelClient.__es is None:
            with ESLowLevelClient.__es_lock:
                if ESLowLevelClient.__es is None:
                    ESLowLevelClient.__es = Elasticsearch(['10.0.2.15'],port=9200,maxsize=25)
                    return ESLowLevelClient.__es

def get(self, index, feature=None, params=None):
    if index in SKIP_IN_PATH:
        raise ValueError("Empty value passed for a required argument 'index'.")
        return self.transport.perform_request("GET", _make_path(index, feature), params=params)

class TestLowLevelClientSearch(unittest.TestCase):
    es = ESLowLevelClient.get_instance()
    def test_match_phrase_query(self):
        body={
            "query": {
                "match_phrase": {
                    "fund_name": {
                        "query": "iShares MSCI ACWI ETF"
                    }
                }
            }
        }
        response = self.es.search(index='cf_etf', body=body)
        self.assertEqual(response['hits']['total']['value'], 1)
        print(response)

def __init__(self):
    raise Exception("This class is a singleton!, use static method 10.0.2.15 getInstance()")
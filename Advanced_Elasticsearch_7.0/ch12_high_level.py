#!/usr/bin/python3

from elasticsearch_dsl import connections
import threading, unittest
from com.example.client.config.low_level_client_by_connection import ESLowLevelClientByConnection
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Q, MatchPhrase

class ESLowLevelClientByConnection:
    __conn = None
    __conn_lock = threading.Lock()
    @staticmethod
    def get_instance():
        if ESLowLevelClientByConnection.__conn is None:
            with ESLowLevelClientByConnection.__conn_lock:
                if ESLowLevelClientByConnection.__conn is None:
                    ESLowLevelClientByConnection.__conn = connections.create_connection('high_level_client', hosts=['10.0.2.15'], port=9200)
                    return ESLowLevelClientByConnection.__conn

    def __init__(self):
        raise Exception("This class is a singleton!, use static method getInstance()")

class Search(Request):
    ...
    def count(self):
        if hasattr(self, '_response'):
            return self._response.hits.total
            es = connections.get_connection(self._using)
            d = self.to_dict(count=True)
            return es.count(index=self._index,
            body=d, **self._params )['count']
            def execute(self, ignore_cache=False):
                if ignore_cache or not hasattr(self, '_response'):
                    es = connections.get_connection(self._using)
                    self._response = self._response_class(
                    self, es.search(index=self._index, body=self.to_dict(), **self._params))
                    return self._response

class TestHighLevelClientSearch(unittest.TestCase):
    def test_match_phrase_query_via_low_level_client(self):
        # call the query method
        search = Search(index='cf_etf',using=ESLowLevelClientByConnection.get_instance()).query('match_phrase', 'fund_name='iShares MSCI ACWI ETF')
        response = search.execute()
        self.assertEqual(response['hits']['total']['value'], 1)
        print(response.to_dict())
def test_match_phrase_query_via_connection(self):
        SLowLevelClientByConnection.get_instance()
        search = Search(index='cf_etf', using='high_level_client')
        # call the Q method
        search.query = Q('match_phrase', fund_name='iShares MSCI ACWI ETF')
        response = search.execute()
        self.assertEqual(response['hits']['total']['value'], 1)
def test_match_phrase_class_via_connection(self):
         ESLowLevelClientByConnection.get_instance()
         # construct the query object using the class of the query type
         search = Search(index='cf_etf', using='high_level_client')
         search.query = MatchPhrase(fund_name='iShares MSCI ACWI ETF')
         response = search.execute()
         self.assertEqual(response['hits']['total']['value'], 1)
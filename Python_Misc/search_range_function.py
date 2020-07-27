#!/bin/python3

'''
search over a range as a function
'''

# imports
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

def es_search(index,field,search_value,start_time,end_time):
    # return the number of hits
    es_search = Search(using=es_conn1, index=index) \
    .filter('range' ,  **{'@timestamp': {'gte': start_time , 'lt':end_time}}) \
    .query({"match": {field:search_value}})
    return es_search.count()

es_conn1 = Elasticsearch([{'host': '10.0.2.15', 'port': 9200}])


if __name__ == '__main__':
    test_search = es_search("messages","origin","kibana","now-1d","now")
    print(test_search)

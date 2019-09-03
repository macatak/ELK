#!/usr/bin/python3.6

'''
just a basic connection script
'''

from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search, Document, Date, Integer, Text

# connect
try:
    es = Elasticsearch(['http://10.0.2.15'], port = 9200)
    print("connection successful")
    print(es.info())
except Exception as ex:
    print("error ")
    print(ex)

# check to see if an index exists
if (es.indices.exists(index="tmdb")):
    print("exists")
else:
    print("does not")

# run a query
s = Search(using=es, index="tmdb") \
    .query('multi_match', fields=["title^10", "overview"], query = 'basketball with cartoon aliens')

# order by score ???
# s = s.highlight_options(order='score')

response = s.execute()

#for hit in response:
    #print(hit['title'])
    # broke      print(['hit._score'], hit.title)


for hit in response['hits']['hits']:
    print(hit['_score'], hit['_source']['title'])


print(type(response))

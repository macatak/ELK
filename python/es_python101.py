#!/usr/bin/python3.6

'''
basic ops
from the 7.0 cookbook
got to page 630
'''

# imports
from elasticsearch import Elasticsearch

#functions

# connect
def connect_to_es():
    try:
        es_connection = Elasticsearch(['http://10.0.2.15'], port = 9200)
        print("connection successful")
        #print(es.info())
        return es_connection
    except Exception as ex:
        print("error ")
        print(ex)

# create an index if it does not already exist
def force_create_index(es, index_name):
    # deletes an index if it already exists
    if es.indices.exists(index_name):
        print('index exists')
    else:
        es.indices.create(index_name)
        es.cluster.health(wait_for_status="yellow")

# create an index but delete it if it already exists
def force_create_index(es, index_name):
    # deletes an index if it already exists
    if es.indices.exists(index_name):
        es.indices.delete(index_name)
    es.indices.create(index_name)
    es.cluster.health(wait_for_status="yellow")

# open an index
def open_index(es, index_name):
    es.indices.open(index_name)
    es.cluster.health(wait_for_status="yellow")

#close an index
def close_index(es, index_name):
    es.indices.close(index_name)

# delete an index
def delete_index(es, index_name):
    if es.indices.exists(index_name):
        es.indices.delete(index_name)

# merge an index
def merge_index(es, inded_name):
    # helps with performance
    es.indices.forcemerge(index_name)

# main program
if __name__ == '__main__':
    # connnect
    es_conn1 = connect_to_es()

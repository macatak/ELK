#!/usr/bin/python3.6

'''
part of a DIY for learning how Python and Elasticsearch play together
mainly for a Relevant Search book that is way out dated
'''

import requests, json

'''
Kibana cURL
curl -XGET "http://10.0.2.15:9200/tmdb/_search" -H 'Content-Type: application/json' -d'{  "explain": true,  "query": {    "multi_match" : {      "query":    "basketball with cartoon aliens",       "fields": [ "title^10", "overview" ]     }  }}'
'''

# replace the '-H' for headers in the cURL for the python request call
headers = {
    'Content-Type': 'application/json',
}

# define the query
# this will be used in place of the '-d' in the request call
query1 = '{"query":{ "multi_match":{ "query":"basketball with cartoon aliens","fields": [ "title^10", "overview" ]}}}'
# query w/ explain
query2 = '{"explain":true, "query":{ "multi_match":{ "query":"basketball with cartoon aliens","fields": [ "title^10", "overview" ]}}}'
#
response = requests.post('http://10.0.2.15:9200/tmdb/_search', data = query1, headers = headers)

# request methods
print(response.text)
print(response.content)

# json methods
jsonResp = json.loads(response.text)
print(jsonResp)
print(type(response))
print(type(jsonResp))

# print it in a better format
json.dumps(jsonResp, indent = 3, separators = [" --- ", " ... "], sort_keys=True)

#print(json.dumps(jsonResp['hits']['hits'][0]['_explanation']))
# print(json.dumps(jsonResp['hits']['hits'][0]))

#responseJson = json.dumps(jsonResp)

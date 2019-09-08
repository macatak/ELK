#!/usr/bin/python3.6

import requests, json

'''
curl -XGET "http://10.0.2.15:9200/tmdb/_search" -H 'Content-Type: application/json' -d'{  "explain": true,  "query": {    "multi_match" : {      "query":    "basketball with cartoon aliens",       "fields": [ "title^10", "overview" ]     }  }}'

'''

# curl -XGET "http://10.0.2.15:9200/tmdb/_search"
headers = {
    'Content-Type': 'application/json',
}

# query1 = '{  "explain": true,  "query": {    "multi_match" : {      "query":    "basketball with cartoon aliens",       "fields": [ "title^10", "overview" ]     }  }}'
query1 = '{"explain":true, "query":{ "multi_match":{ "query":"basketball with cartoon aliens","fields": [ "title^10", "overview" ]}}}'
# -d is data
#
response = requests.post('http://10.0.2.15:9200/tmdb/_search', data = query1, headers = headers)

print(response.text)
print(response.content)

#print(json.loads(response.text))

jsonResp = json.loads(response.text)
#print(json.dumps(jsonResp['hits']['hits'][0]['_explanation']))
print(json.dumps(jsonResp['hits']['hits'][0]))

responseJson = json.dumps(jsonResp)

'''
#for hit in responseJson['hits']['hits']:
for hit in responseJson:
    #print(hit['_score'], hit['_source']['title'])
    print(hit['_score'][0])
'''

'''
print(httpResp.text)
print(type(httpResp))
validation = httpResp.json
print(validation)
# httpResp.Header.Set("Content-Type", "application/json")
print(json.loads(httpResp.text))
# print(json.loads(httpResp.text))
'''

#!/usr/bin/python3

# tutorial
# https://developers.themoviedb.org/3/getting-started/introduction

'''
Python script to create a readable JSON file for Logstash to consume
Mainly did this for 'Relevant Search' book which has code that does not work
    with current versions of Python and ELK
'''

import requests
# import json
import time

'''
To-DO
- write the valid index arguments to a file, then we could read from that File
    this would speed it up
- Use Python's JSON library
    not sure how this plays with Logstash but it's the right way to do it
- Make these function calls and not a top down script
'''

# set the TMDB API key
api_key='<your API key here>'

long_delay=15   # used if rate limit is about used up
short_delay= 0   # used  as a generic delay

# index sizes, think max_indice will take ~2 days given rate limiting
max_index=576594    # this is the latest index (1/2019)
index=1000

# write to a File
# naming this based on how many records we'll pull down
# file does not need to exist but the path should
# path = '/home/zaphod/tmdb_1/test_10.json'
path = '/home/zaphod/tmdb_1/test_50K-300K.json'
tmdb_out = open(path,'w')

# range can be whatever we want
# format is range(start_value, end_value)
# this won't be an actual count of records returned
# due to invalid index arguments
for idx in range(50000, 200000):
    print("trying index - {}".format(idx))
    resp1 = requests.get('https://api.themoviedb.org/3/movie/' + str(idx) + '?api_key=' + api_key)
    #print(resp1.text)
    #print(resp1.status_code)
    # check the status code for a valid index
    if resp1.status_code == 200:
        # write it to the file with a newline
        # may not need to newline but this worked for a Logstash input
        tmdb_out.write(resp1.text + '\n')
        # check the rate limit left and delay if we're pushing it
        rate_limit = resp1.headers["X-RateLimit-Remaining"]
        print("rate limit : {}".format(rate_limit))
        #print(rate_limit)
        if int(rate_limit) <= 2:
            time.sleep(long_delay)
        else:
            time.sleep(short_delay)

# close the file becuase it's a good practice
tmdb_out.close

#!/usr/bin/python3

'''
basicPython script to write to OpenSearch
uses some CSV from /python/logFileGenerator
'''
# imports
from datetime import datetime
from random import randint
from opensearchpy import OpenSearch
import csv, random, time

# functions
def createLogLevel():
    # return a standard log level
    # weighted on a sale of 0-100 so most should be info
    ranLogLevelNumber = random.randint(0, 100)
    if ranLogLevelNumber >= 0 and ranLogLevelNumber <= 70:
        logLevel = "info"
    elif ranLogLevelNumber >= 71 and ranLogLevelNumber <= 75:
        logLevel = "debug"
    elif ranLogLevelNumber >= 76 and ranLogLevelNumber <= 80:
        logLevel = "trace"
    elif ranLogLevelNumber >= 81 and ranLogLevelNumber <= 85:
        logLevel = "warn"
    elif ranLogLevelNumber >= 86 and ranLogLevelNumber <= 90:
        logLevel = "error"
    elif ranLogLevelNumber >= 91 and ranLogLevelNumber <= 99:
        logLevel = "critical"    
    else:
        logLevel = "fatal " #  + str(ranLogLevelNumber)    
    return logLevel
def get_random_item(list_name, random_range):
    '''
    return a random item from a list
    '''
    ran = random.randint(1,random_range)
    return list_name[ran]
def read_csv(csvFilename, row_number):
    '''
    read a CSV file into a list
    args are filename and row of the desired item
    '''

    with open(csvFilename) as f:
        # list object to return
        return_list = []
        # open the file which returns a pointer to the 1st line
        reader = csv.reader(f)
        # this will move the pointer to the next line so it skips the header line of the CSV
        next(reader)
        for row in reader:
            # print it if you want
            # print(row[row_number])
            # add it to a list
            return_list.append(row[row_number])
    return return_list


if __name__ == '__main__':
    # variables
    host = [{'host': '127.0.0.1', 'port': 9200}]
    auth = ('admin', 'admin')
    ca_certs_path = '/home/bikeride/opensearch/opensearch-2.1.0/config/root-ca.pem'
    target_index = 'test_index1'
    client = OpenSearch(hosts=host,http_compress=True,http_auth=auth,use_ssl=True,verify_certs=True,ssl_assert_hostname=False,ssl_show_warn=False,ca_certs=ca_certs_path)
    # target index to write to
    target_index = 'test_index1'
        # generate lists from CSV files
    messageList = read_csv("/home/bikeride/Documents/csvFiles/Human-to-HumanActionableRequestsDataset.csv", 1)
    msgTypeList = read_csv("/home/bikeride/Documents/csvFiles/Human-to-HumanActionableRequestsDataset.csv", 0)
    msgDirectionList = read_csv("/home/bikeride/Documents/csvFiles/Human-to-HumanActionableRequestsDataset.csv", 2)
    msgValidtyList = read_csv("/home/bikeride/Documents/csvFiles/Human-to-HumanActionableRequestsDataset.csv", 3)

    for i in range(100):
        loglevel = createLogLevel()
        message = get_random_item(messageList, len(messageList) -1)
        msgType =  get_random_item(msgTypeList, len(msgTypeList) -1)
        msgDirection =  get_random_item(msgDirectionList, len(msgDirectionList) -1)
        msgValidity = get_random_item(msgValidtyList, len(msgValidtyList) -1)
        today = datetime.now()
        iso_datetime = today.isoformat()
        # set up the event
        document = {
            'time_stamp' : iso_datetime,
            'msg': message,
            'msg_type': msgType,
            'msg_direction': msgDirection,
            #'msg_validity': msgValidity,
            'log_level': loglevel
            }
        # send a write request
        response = client.index(
            index = target_index,
            body = document,
            refresh = True
            )
        # print the response if you want
        print(response)
        # short random delay
        time.sleep((random.random()))

#!/usr/bin/python3

'''
Basic OpenSearch connection
'''
from opensearchpy import OpenSearch

host = [{'host': '127.0.0.1', 'port': 9200}]
auth = ('admin', 'admin')
ca_certs_path = '/home/bikeride/opensearch/opensearch-2.1.0/config/root-ca.pem'
target_index = 'test_index1'
client = OpenSearch(hosts=host,http_compress=True,http_auth=auth,use_ssl=True,verify_certs=True,ssl_assert_hostname=False,ssl_show_warn=False,ca_certs=ca_certs_path)

print(client.info())
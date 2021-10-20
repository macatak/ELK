# OpenSearch Repo  
OpenSearch is a fork of Elasticsearch so goal is to set it up on a VM.  
Docker is easy but I use VM's at work so this is the start of figuring it out  
NOTE - Validated on version 1.1.0

## Opensearch setup
- Navigate to [OpenSearch Download](https://artifacts.opensearch.org/releases/bundle/opensearch/1.1.0/opensearch-1.1.0-linux-x64.tar.gz)
- Extract the TAR file
- *tar -zxf opensearch-1.1.0-linux-x64.tar.gz*
- cd into opensearch-1.1.0/bin
- Remove the security plugin since it errors out
- *./opensearch-plugin remove opensearch-security* 
- Edit the opensearch-1.1.0/config/opensearch.yml. [This](https://github.com/macatak/ELK/blob/master/ymls/elasticsearch_ver7.yml) will work but change the IP address or set it to localhost
- Run *opensearch-1.1.0/bin/opsensearch*
- Go to the IP:9200 or localhost:9200, depending on how the opensearch.yml is set, in a browser and you should see the OpenSearch page



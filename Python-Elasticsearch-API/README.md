# Elasticsearch Python API
- This is the low level API and the search (elasticsearch-dsl)
- Main use case is automating health checks and other low level functions
- There is some basic search but not a lot  
API link _https://elasticsearch-py.readthedocs.io/en/master/api.html_

## elasticsearch_dsl API

### Basic Connection
- Just basic connection in the [DSL-Basic Connection](https://github.com/macatak/ELK/blob/master/Python-Elasticsearch-API/dsl_basicConnection.ipynb). Some things unproven (like conectioning to multiple clusters)

### Basic Search
- Some [Basic Search operations](https://github.com/macatak/ELK/blob/master/Python-Elasticsearch-API/dsl_search_101.ipynb). Shows how to access the values returned

## Low level API

### Setup
- Run the [Star Wars Setup](https://github.com/macatak/ELK/blob/master/Python-Elasticsearch-API/ElasticsearchLoadStarWars.ipynb) notebook. This will setup a few indices using the Star Wars API. Most of the examples use one of those indices  
- If you don't want to see all the print statements comment them out. The notebook has them all included so it's a good example of what you should see. It's a little verbose but I like seeing an indication something is happening  
- I use VirtualBox and run the stack on a VM. I do not use localhost but run Elasticsearch on an IP

### [Cluster Ops API](https://github.com/macatak/ELK/blob/master/Python-Elasticsearch-API/ElasticsearchPythonClusterOps.ipynb)
- Basic cluster info and health checks

### [Index Info API](https://github.com/macatak/ELK/blob/master/Python-Elasticsearch-API/ElasticsearchPythonIndexInfo.ipynb)
- Basic index information like size, doc count, average document size, etc.

### [Index Ops API](https://github.com/macatak/ELK/blob/master/Python-Elasticsearch-API/ElasticsearchPythonIndexOps.ipynb)
- Contans basic index operations
- open, close, create, delete, check exists, flush, force merge, refresh, shard store info, segment info, shrink (in progress), operations status.  

### [Node Ops API](https://github.com/macatak/ELK/blob/master/Python-Elasticsearch-API/ElasticsearchPythonNodeOps.ipynb)
- Node information like allocations, shards, disk space etc.
- Needs some more work since this was tested on a single node stack

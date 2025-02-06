from elasticsearch import Elasticsearch as es

search = es('http://localhost:9200')
clientInfo = search.info()
print(clientInfo.body)

search.indices.create(index="my_index", settings={"index":{"number_of_replicas":1,"number_of_shards":3}}) # Replica is the copies of data, shards is the data segments


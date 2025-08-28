# Log-Collector
## Create topic in Kafka
### start Kafka and Zookeeper
```
docker-compose up -d
```
### enter kafka container
```
docker exec -it kafka bash
```
### create a topic
```
kafka-topics --create --topic logs --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
## receive message from topic
### start server
```
uvicorn main:app --reload
```
### open consumer terminal
```
python consumer.py
```
## useful command
```
docker-compose logs kafka
docker ps -a
docker-compose down # delete container
kafka-topics --list --bootstrap-server localhost:9092
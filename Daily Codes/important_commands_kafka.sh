sudo systemctl start confluent-zookeeper
sudo systemctl status confluent-zookeeper

sudo systemctl start confluent-kafka
sudo systemctl status confluent-kafka

sudo systemctl start confluent-kafka-connect
sudo systemctl status confluent-kafka-connect

sudo systemctl start confluent-schema-registry
sudo systemctl status confluent-schema-registry

kafka-topic --version

kafka-topics --bootstrap-server localhost:9092 --topic example_topic --create --partitions 1 --replication-factor 1
kafka-topics --bootstrap-server localhost:9092 --list
kafka-topics --bootstrap-server localhost:9092 --describe
kafka-topics --bootstrap-server localhost:9092 --topic example_topic --describe

kafka-console-producer --bootstrap-server localhost:9092 --topic example_topic
kafka-console-producer --bootstrap-server localhost:9092 --topic example_topic --property parse.key=true --property key.separator=:

kafka-console-consumer --bootstrap-server localhost:9092 --topic example_topic
kafka-console-consumer --bootstrap-server localhost:9092 --topic example_topic --from-beginning --property print.key=true

curl -X GET http://localhost:8083/connector-plugins
curl http://localhost:8083/connectors/file_source_connector
curl http://localhost:8083/connectors/file_source_connector/status

curl -X DELETE http://localhost:8083/connectors/file_source_connector

kafka-console-producer --bootstrap-server localhost:9093 --topic example_topic --producer.config client-ssl.properties
kafka-console-consumer --bootstrap-server localhost:9093 --topic example_topic --from-beginning --consumer.config client-ssl.properties

kafka-console-producer --bootstrap-server localhost:9094 --topic example_topic --producer.config client-sasl.properties
kafka-console-consumer --bootstrap-server localhost:9094 --topic example_topic --from-beginning --consumer.config client-sasl.properties

sudo nano /etc/kafka/server.properties
sudo nano client-ssl.properties
sudo nano client-sasl.properties

sudo find / -name '*schema-registry*.properties'
sudo tail -f /var/log/kafka/server.log
sudo tail -n 50 /var/log/kafka/server.log
sudo netstat -tuln
sudo netstat -tunap

kafka-acls --authorizer-properties zookeeper.connect=localhost:2181 --add --allow-principal User:Platformatory --operation all --topic acl-test

git branch
git checkout scenario3
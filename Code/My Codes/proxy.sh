Begin by logging in to the lab servers using the credentials provided on the hands-on lab page:

ssh cloud_user@PUBLIC_IP_ADDRESS

Publish the Missing Records to the inventory_purchases Topic

    Publish the records using an HTTP request to Confluent REST Proxy:

curl -X POST -H "Content-Type: application/vnd.kafka.json.v2+json" \
  -H "Accept: application/vnd.kafka.v2+json" \
  --data '{"records":[{"key":"apples","value":"23"},{"key":"grapes","value":"160"}]}' \
  "http://localhost:8082/topics/inventory_purchases"

    We can verify that the data is in the topic with a console consumer:

kafka-console-consumer --bootstrap-server localhost:9092 --topic inventory_purchases --from-beginning --property print.key=true

Note: We should see the processed total of 2 messages.
Publish the Missing Records to the member_signups Topic

    Publish the records using an HTTP request to Confluent REST Proxy:

curl -X POST -H "Content-Type: application/vnd.kafka.json.v2+json" \
  -H "Accept: application/vnd.kafka.v2+json" \
  --data '{"records":[{"key":"77543","value":"Rosenberg, Willow"},{"key":"56878","value":"Giles, Rupert"}]}' \
  "http://localhost:8082/topics/member_signups"

    We can verify that the data is in the topic with a console consumer:

kafka-console-consumer --bootstrap-server localhost:9092 --topic member_signups --from-beginning --property print.key=true

Note: We should see the processed total of 2 messages.
Conclusion

Congratulations - you've completed this hands-on lab!
Real time data streaming pipeline

Airflow triggers the job that gets the data form API and streams it using Kafka Producer to the broker
A Spark session is created that connects with the kafka broker and subscribes to the topic
The data from the topic is streamed and stored in Cassandra table
The pipeline is created in a dockerized enviroment



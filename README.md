# Real-Time Stock Data Pipeline with Kafka & AWS: From Ingestion to Insight

Inspirations from [@airscholar's]([airscholar](https://github.com/airscholar)) project on [data-engineering](https://github.com/airscholar/e2e-data-engineering)

This project demonstrates a data streaming pipeline using Kafka, Spark, and Cassandra. The pipeline reads data from a Kafka topic, processes it using Spark, and stores the results in a Cassandra database.

## Project Structure

```txt
dags/
|-- kafka_stream.py
script/
|-- entrypoint.sh
docker-compose.yml
README.md
requirements.txt
spark_stream.py
```

## Prerequisites

- Docker and Docker Compose
- Python 3.8+
- Apache Kafka
- Apache Spark
- Cassandra

## Setup

### Docker

1. Build and start the Docker containers:

    ```sh
    docker-compose up --build
    ```

2. This will start the following services:
    - Kafka
    - Spark
    - Cassandra

### Python

1. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Kafka Stream

The Kafka stream is handled by the script [`kafka_stream.py`](.dags/kafka_stream.py). It formats the incoming data from Kafka.

### Spark Stream

The Spark stream is handled by the script [`spark_stream.py`](./spark_stream.py). It performs the following tasks:

- Creates a Spark connection
- Connects to Kafka
- Processes the data
- Writes the data to Cassandra

### Entrypoint Script

The entrypoint script [`entrypoint.sh`](./script/entrypoint.sh) initializes the Airflow database and creates an admin user.

## Configuration

The configuration for the Docker services is defined in [`docker-compose.yml`](./docker-compose.yml)

## Running the Pipeline

1. Start the Docker containers:

    ```sh
    docker-compose up
    ```

2. Run the Spark streaming job:

    ```sh
    python script/spark_stream.py
    ```
